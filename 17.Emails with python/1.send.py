import smtplib
smtp_object=smtplib.SMTP('smtp.gmail.com')
smtp_object.ehlo()
smtp_object.starttls()
#Use getpass library to hide password input
import getpass
#Login
email=getpass.getpass("Enter your email: ")
password=getpass.getpass("Enter the password: ")
print(smtp_object.login(email,password))
#Message composition
from_address=email
To_address=input("Enter the address to be sent to: ")
Subject=input("Enter the subject line: ")
body=input("Enter the body message: ")
message="Subject: "+Subject+"\n"+body
#Sending
print(smtp_object.sendmail(from_address,To_address,message))


