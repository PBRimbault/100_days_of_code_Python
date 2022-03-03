import pandas as pd
import datetime as dt
import smtplib
import random
import os

# 2. Check if today matches a birthday in the birthdays.csv
df = pd.read_csv('birthdays.csv')
now = dt.datetime.now()
birthday_names = []

my_email = "patrick.rimbault@gmail.com"
password = "szibuwnbjefidhne"

for index, row in df.iterrows():
    if row['day'] == now.day and row['month'] == now.month:
        birthday_names.append(row['name'])
    
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
for person in birthday_names:
    letter_file = random.choice(os.listdir('letter_templates'))
    file = open(f'letter_templates/{letter_file}', 'r')
    blank_letter = file.read()
    edited_letter = blank_letter.replace("[NAME]", person)
    file.close()
# 4. Send the letter generated in step 3 to that person's email address.

    with smtplib.SMTP("smtp.gmail.com") as connection:            
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email, 
                to_addrs="patrick@njvconsulting.co.za", 
                msg=f"Subject:Happy Birthday {person}!\n\n{edited_letter}"
                )