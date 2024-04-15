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
auth_token = '###'

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
data_alpha = response_alpha.json()['Time Series (Daily)']
data_list = [value for (key, value) in data_alpha.items()]

yesterday_closing = float(data_list[0]['4. close'])
day_before_yesterday_closing = float(data_list[1]['4. close'])

# check the percentage change between yesterday to today
price_difference = abs(yesterday_closing - day_before_yesterday_closing)
percent_change = 100 * price_difference / day_before_yesterday_closing
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