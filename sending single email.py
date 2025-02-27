import yagmail
from settings import password,email

SENDER_EMAIL = email
RECEIVER_EMAIL = "awortwedanieljr15@gmail.com"

SUBJECT = "Good morning!"

CONTENTS = "Hi!"

yag = yagmail.SMTP(user=SENDER_EMAIL, password=password)
yag.send(to=RECEIVER_EMAIL, subject=SUBJECT, contents=CONTENTS)
print("Email sent!!")
