import re
#Other regex syntax
results=re.search(r"cat|dog","Have you seen my dog?")
print(results)
results=re.findall(r"at","The cat at my house sat in the hat there")
print(results)
results=re.findall(r".at","The cat at my house sat in the hat there")
print(results)
results=re.findall(r"^\d","1 is a number")
print(results)
results=re.findall(r"\d$","A number which is equal to 2")
print(results)
results="There are 3 numbers in this sentence namely 34 and 5 "
pattern=r'[^\d]+'
results=re.findall(pattern,results)
print(results)
test_phrase="This is a string! with ponctuations.is it true?"
results=re.findall(r'[^!.? ]+',test_phrase)
print(results)
print(' '.join(results))
text="Only find the hyphen-dash words in this sentence. But you do not know how long-ish they are."
pattern=r'[\w]+-[\w]+'
results=re.findall(pattern,text)
print(results)

t1="I saw a catfish yesterday"
t2="I have a caterpiler at home"
t3="Would you like to take a catnap right now?"
r1=re.search(r'cat(fish|erpiler|nap)',t1)
r2=re.search(r'cat(fish|erpiler|nap)',t2)
r3=re.search(r'cat(fish|erpiler|nap)',t3)
print(r1.group())
print(r2.group())
print(r3.group())