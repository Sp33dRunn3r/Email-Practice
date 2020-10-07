Using Python for Emails:
import smtplib
from email.message import EmailMessage
from string import Template

email = EmailMessage()
email['from'] = 'Maxwell Hollins'
email['to'] = 'cmaxwellhollins@gmail.com'
email['subject'] = 'You won... a decent career!!!'

email.set_content('I am a Python Master!')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('python3tester1@gmail.com', 'hollins20!')
    smtp.send_message(email)
    print('all good boss!')
