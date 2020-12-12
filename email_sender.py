#This piece of code enables one to send emails with python
#Useful links below
'''
		https://www.geeksforgeeks.org/simple-mail-transfer-protocol-smtp/
		https://docs.python.org/3/library/email.html#module-email
		https://docs.python.org/3/library/email.examples.html
'''

'''
import smtplib #simple mail transfer protocol (smtp)
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'NAME' #Name of sender
email['to'] = 'EMAIL ADDRESS' #Email address the email will be sent to
email['subject'] = 'WINNER'

email.set_content('I am a Python Master.') #Well, atleast I think I am :)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:#hosts port value differ/check your email server
	smtp.ehlo() #protocol of the method ##here I connected to the server
	smtp.starttls()#to connect securely to the server ##connected to the server
	smtp.login('EMAIL ADDRESS', 'PASSWORD')#login to your account 
	smtp.send_message(email)#send the email 
	print('All good boss!')
'''

#MORE ON SENDING EMAILS 
'''
This is an improvement of the program above.
Instead of just sending a generic email, I want to customize it to each individual
Imagine having a database of users with their email addresses and first names.
Ideally I woudld be able to customize the email to each specific person.
And that can be done by using an html based email.
So I can send text emmails(that just have text) or even something more dynamic like html
'''

import smtplib
from email.message import EmailMessage
from string import Template #making good use of the string.template class
from pathlib import Path #this is similar to the os.path and it enables me to access the 'index.html' file(attached to project)

html = Template(Path('index.html').read_text()) #read_text() to read the 'index.html' path 
email = EmailMessage()
email['from'] = 'NAME'
email['to'] = 'EMAIL ADDRESS'
email['subject'] = 'You won 1,000,000 dollars!'#Familiar spam email subject?

email.set_content(html.substitute({'name': 'TinTin'}), 'html') 
'''
		Assigned 'name' which is in the 'index.html' file as TinTin-could me anything really.
		The second parameter 'hmtl' confirms that this is in hmtl
																
'''
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login('EMAIL ADDRESS', 'PASSWORD')
  smtp.send_message(email)
  print('All good boss!')