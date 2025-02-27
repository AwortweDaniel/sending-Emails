import yagmail
from settings import *
import pandas as pd

content = "kindly sleep!!"

contact_list = pd.read_csv("contactList.csv")
print(contact_list)
yag = yagmail.SMTP(email, password)

for index, row in contact_list.iterrows():
    subject = f"Sunny afternoon, {row["name"]}"
    yag.send(to=row["email"], subject=subject, contents=content)
    print("Email sent successfully!!")