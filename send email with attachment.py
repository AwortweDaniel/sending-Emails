import yagmail
from settings import password,email

receiver = "awortwedanieljr15@gmail.com"

SUBJECT = "Good afternoon!"

CONTENTS = ["Useful quotes", "quotes.txt"]

yag = yagmail.SMTP(user=email, password=password)
yag.send(to=receiver, subject=SUBJECT, contents=CONTENTS)
print("Email sent!!")
