from ast import stmt
import email
import smtplib
from email.message import EmailMessage
from turtle import stamp
email_1= EmailMessage()
email_1["FROM"]="Mahmoud Elkout"
email_1["TO"]="mahmoud.mohamed.ali.hack.1970@gmail.com"
email_1["Subject"]="TRY TO SEND MAIL"
email_1.set_content("HI,Budy HOW ARE YOU?!! I hope You Are Fine \nThanks Alot.")
with smtplib.SMTP(host="smtp.gmail.com",port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("engmahmoudaliahmed2@gmail.com","Sad1234567")
    smtp.send_message(email_1)
    print("all good Boss")


