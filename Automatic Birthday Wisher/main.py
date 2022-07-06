##################### Automatic Birthday Wisher ######################

import datetime as dt
import pandas
import random
import smtplib

#Checking current month and date
today = (dt.datetime.now().month,dt.datetime.now().day)

#Looking at CSV file with birthday people's info
birthdays_file = pandas.read_csv("birthdays.csv")
birthdays_dict = {(row["month"],row["day"]): row for (index,row) in birthdays_file.iterrows()}

#Checks if today matches anyone's birthday in birthday people's info
if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    #If so, randomly choose a letter format between letters 1,2, or 3 .txt
    letter_file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(letter_file_path) as random_letter_format:
        content = random_letter_format.read()
        #Change the placeholder of the name to the actual name of the person
        letter = content.replace("[NAME]",birthday_person["name"])

    #Begin the process of sending the email out
    with (smtplib.SMTP("smtp.gmail.com",587)) as email_data:
        email_data.starttls()
        email_data.login(user="progrmstnd790@gmail.com",password="xfxkvvvopdgjkbcy")
        email_data.sendmail(from_addr="progrmstnd790@gmail.com",to_addrs=birthday_person["email"],msg=letter)
# 4. Send the letter generated in step 3 to that person's email address.
# HINT 1: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
# HINT 2: Remember to call .starttls()
# HINT 3: Remember to login to your email service with email/password. Make sure your security setting is set to allow less secure apps.
# HINT 4: The message should have the Subject: Happy Birthday then after \n\n The Message Body.



