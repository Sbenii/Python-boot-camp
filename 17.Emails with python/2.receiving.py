import imaplib
M=imaplib.IMAP4_SSL("imap.gmail.com")
import getpass
email=getpass.getpass("Enter enail: ")
password=getpass.getpass("Enter password: ")
print(M.login(email,password))
M.list()
M.select('Inbox')
typ, data=M.search(None,'SUBJECT "WOE!"')
email_id=data[0]
print(email_id)
result, email_data=M.fetch(email_id,"(RFC822)")
raw_email=email_data[0][1]
raw_email_string=raw_email.decode("utf-8")
import email
email_message=email.message_from_string(raw_email_string)
 
for part in email_message.walk():
    if part.get_content_type()=='text/plain':
        body=part.get_payload(decode=True)
        print(body)
    
'''
email_ids=data[0].split()
id=email_ids[0]
This is used when having many Ids for the same subject!!!
'''
