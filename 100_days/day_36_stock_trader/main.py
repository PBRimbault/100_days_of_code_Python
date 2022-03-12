import requests
from datetime import datetime as dt
from datetime import timedelta
from datetime import date

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

alpha_vantage_api = '0932AKBUWY8FBQC7'

## STEP 1: Use https://www.alphavantage.co/query
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 

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

if percent_change > 5:
    print("Get news")


## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator


# Set the parameters for the API call to NewsAPI
news_parameters = {
    "key": 'value',   
}

# Do the API call to NewsAPI
response_news = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
response_news.raise_for_status()

# Convert the API response to JSON format
data_news = response_news.json()

## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

