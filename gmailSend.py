#Import libraries
import smtplib
from email.mime.text import MIMEText


userGmail = input('What is your email address? (GMail only)')
password = input('What is your GMail password? ')
recipientEmail = input("What is the recipient's email address? ")
messageSubject = input('What is the subject of this message? ')
messageText = input('What is the message?')

#Compose message
msg = MIMEText(messageText)
msg['Subject'] = messageSubject
msg['From'] = userGmail
msg['To'] = recipientEmail

#Create & login to gmail server.  Send message.
s = smtplib.SMTP('smtp.gmail.com', 587)
s.ehlo()
s.starttls()
s.login(msg['From'], password)
s.send_message(msg)

s.quit()
