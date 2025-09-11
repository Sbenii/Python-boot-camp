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
phone=re.search(r"\d{3}-\d{3}-\d{4}",text)#--->usinf quantifiers
#the compile function
phone_pattern=re.compile(r'(\d{3})-(\d{3})-(\d{4})')
results=re.search(phone_pattern,text)
print(results.group())
print(results.group(1))
print(results.group(2))
print(results.group(3))