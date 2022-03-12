import requests
from datetime import datetime as dt
from datetime import timedelta
from datetime import date
from twilio.rest import Client


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

alpha_vantage_api = '0932AKBUWY8FBQC7'
news_api = 'a78b5461dc7b46ae8fc2cdfc36c7c673'

account_sid = 'ACc50768f767887369eba0020f64a6b7d5'
auth_token = '64855baa05b7b7b5f3d124d25a416ebd'

# Set the parameters for the API call to alphavantage
alpha_parameters = {
    "function": 'TIME_SERIES_DAILY',
    "symbol": STOCK,
    "exclude": 'current,minutely,daily',
    "apikey": alpha_vantage_api
}

# Do the API call to alphavantge
response_alpha = requests.get(url=STOCK_ENDPOINT, params=alpha_parameters)
response_alpha.raise_for_status()

# convert the API response to JSON format
data_alpha = response_alpha.json()

def latest_business_day(check_day):
    # check if the check_day argument is a weekday and if not, roll back to previous business day (Mon - Fri)
    if date.weekday(check_day) == 5:      #if it's Saturday
        check_day = check_day - timedelta(days = 1) #then make it Friday
    elif date.weekday(check_day) == 6:      #if it's Sunday
        check_day = check_day - timedelta(days = 2); #then make it Friday
    return check_day

# Pass today - 1 day to latest_business_day to check if it's a business day. The - 1 is because often RSA today is ahead of closing in USA
this_day = dt.today() - timedelta(days = 1)
lastBusDay = latest_business_day(this_day)
# Pass yesterday to latest_business_day to check if it's a business day.
previousDay = latest_business_day(lastBusDay) - timedelta(days = 1)
# Convert days to string date format to check the JSON dictionary
lastBusDate = lastBusDay.strftime("%Y-%m-%d")
previousDate = previousDay.strftime("%Y-%m-%d")

# Get the closing prices for today and yesterday
today_price = float(data_alpha['Time Series (Daily)'][lastBusDate]['4. close'])
yesterday_price = float(data_alpha['Time Series (Daily)'][previousDate]['4. close'])

# check the percentage change between yesterday to today
price_difference = abs(today_price - yesterday_price)
percent_change = 100 * price_difference / yesterday_price
print(f'Percent change: {percent_change}')



def get_news():

    # Set the parameters for the API call to NewsAPI
    news_parameters = {
        'q': COMPANY_NAME,
        'pageSize': 3,
        "apiKey": news_api,   
    }

    # Do the API call to NewsAPI
    response_news = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    response_news.raise_for_status()

    # Convert the API response to JSON format
    data_news = response_news.json()
    articles = data_news['articles']
    # print(articles)

    for item in articles:

        headline = item['title']
        brief = item['content']
        link = item['url']

        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
                    body=f"{STOCK}: {percent_change}\nHeadline: {headline}\nLink: {link}",
                    from_='+17047033036',
                    to='+27716067067'
                )

if percent_change > 5:
    print('Will send the SMS through')
    get_news()