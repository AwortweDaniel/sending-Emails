from smtplib import SMTP
from settings import *
import time
import random


receiver = ["awortwedanieljr15@gmail.com", "enockawor@gmail.com"]
subject = "Today is Wednesday"

count = 5
while count > 0:
    count -= 1
    with open("quotes.txt", "r") as file:
        fs = file.readlines()
        c = [f.split("\n") for f in fs]
        content = random.choice(c)

    with SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(email, password)
        for i in receiver:
            connection.sendmail(from_addr=email, to_addrs=i, msg=f"Subject:{subject}\n\n{content}")
        print("Email sent!!")
        time.sleep(10)
