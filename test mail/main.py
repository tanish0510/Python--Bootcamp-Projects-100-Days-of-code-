import datetime as dt
import random
import smtplib

MY_EMAIL = "tanishseth0510@gmail.com"
PASSWORD = "nfnlkqpleyyodzdv"
now=dt.datetime.now()
weekday=now.weekday()
if weekday==1:
    with open("quotes.txt") as quotes:
        all_quotes=quotes.readlines()
        random_quote=random.choice(all_quotes)
    print(random_quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="akritikhandelwal20@gmail.com",
                            msg=f"Subject: Motivational Quote\n\n{random_quote}"
                            )
