import smtplib
import datetime as dt
import random

my_email = "patrick.rimbault@gmail.com"
password = "szibuwnbjefidhne"
now = dt.datetime.now()

with open('quotes.txt', 'r') as f:
    quotes_list = f.readlines()

if now.weekday() == 2:
    quote = random.choice(quotes_list)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        # Server name: smtp.office365.com
        # Port: 587
        # Encryption method: STARTTLS
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs="patrick@njvconsulting.co.za", 
            msg=f"Subject:Motivational quote\n\n{quote}"
            )
