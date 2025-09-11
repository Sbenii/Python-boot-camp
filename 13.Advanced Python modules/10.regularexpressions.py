text="The agent's phone number is 255-345-5500. Call soon!!"
import re
pattern='phone'
print(re.search(pattern,text))

match=re.search(pattern,text)
print(match.span())
print(match.start())
print(match.end())
myli="My phone, my phone where is you my phone??"
matches=re.findall('phone',myli)
print(matches)
print(len(matches))
for matches in re.finditer(pattern,myli):
    print(matches)