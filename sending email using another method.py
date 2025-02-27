from smtplib import SMTP
from settings import *
from _datetime import datetime
import time

today = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
receiver = "awortwedanieljr15@gmail.com"
subject = "Bright Morning"
content = f"Today is {today}"


count = 0
while count < 5:
    count += 1
    with SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(email, password)
        connection.sendmail(from_addr=email, to_addrs=receiver, msg=f"subject:{subject}\n\n{content}")
        print("Email sent!!")
        time.sleep(5)
