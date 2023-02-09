from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'dmtareq45@gmail.com'
password = 'ouyopoiomadadcfsfrer'

email_receiver = 'walolo4397@tohup.com'

subject = 'Greetings'

body = """
        Hi there!
        How are you??
        
"""

em = EmailMessage()
em['from'] = email_sender
em['to'] = email_receiver
em['SUBJECT'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
