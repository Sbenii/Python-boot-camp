import re
'''
/d-->digit
/w-->alphanumeric
/s-->white space
/D-->non digit
/W-->non alphanumeric
/S-->non whitespace 
'''
text='My phone number is 408-555-7777'
phone=re.search(r"\d\d\d-\d\d\d-\d\d\d\d",text)
print(phone.group())
