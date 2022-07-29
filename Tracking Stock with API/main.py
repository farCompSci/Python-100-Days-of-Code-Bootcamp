import requests
import datetime as dt
import os
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
stock_api_key = "Input API KEY" #Removed for safety
news_api = "Input API KEY" 

stock_parameters = {
    "function":"TIME_SERIES_DAILY",
    "symbol":"TSLA",
    "apikey":stock_api_key
}

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
"""Yesterday's date"""
today = dt.date.today()
yesterday = today - dt.timedelta(days=1)
day_before_yesterday = yesterday - dt.timedelta(days=1)

"""Gets all the api data for Tesla Stocks"""
stock_data_api = requests.get(STOCK_ENDPOINT,params=stock_parameters)
stock_data_api.raise_for_status()
tesla_stock_data = (stock_data_api.json())

"""Yesterday's Stock Closing"""
closing_price_yesterday = float(tesla_stock_data['Time Series (Daily)'][str(yesterday)]['4. close'])

#TODO 2. - Get the day before yesterday's closing stock price

"""Day Before Yesterday's Closing"""
closing_price_bf_yesterday = float(tesla_stock_data['Time Series (Daily)'][str(day_before_yesterday)]['4. close'])

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

"""Difference Between Yesterday and Day Before"""
change_in_stock_price = abs(closing_price_bf_yesterday - closing_price_yesterday)

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

"""Change in percentage"""
percentage_difference = (change_in_stock_price/closing_price_yesterday) * 100

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").


# if percentage_difference >= 5:
#     print("Get News")

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

"""Getting News API Info"""

def get_news():
    news_parameter = {
        "q":"tesla",
        "from":"2022-05-30",
        "sortBy":"publishedAt",
        "apiKey":news_api
    }

    news_data_api = requests.get("https://newsapi.org/v2/everything",params=news_parameter)
    news_data_api.raise_for_status()
    tesla_news_data = news_data_api.json()
    three_first_articles = tesla_news_data['articles'][:3]
    return three_first_articles

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
if percentage_difference >= 5.0:
    get_news()

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
#Done in previous TODO

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

def prepare_text_content():
    news_array = get_news()
    final_array = [(news_array[_]['title'],news_array[_]['description']) for _ in range(len(news_array))]
    return final_array


text_array = prepare_text_content()

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
#Done in previous TODO

#TODO 9. - Send each article as a separate message via Twilio.
account_sid : str #<input account_sid here>
auth_token : str #<input auth_token here>

def send_articles(text_content):
    for element in text_content:
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body=f"Headline: {element[0]}\nBrief: {element[1]}",
            from_="input twilioNumber", #Removed for privacy
            to="+261329375832",
        )
        print(message)

send_articles(text_array)

#Optional TODO: Format the message like this: 

