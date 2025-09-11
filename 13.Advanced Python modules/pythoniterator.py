'''
with open("Instructions.txt") as f:
    content=f.read()
    print(content)
'''
import re

def search(file,pattern=r'\d{3}-\d{3}-\d{4}'):
    f=open(file,'r')
    text=f.read()
    
    if re.search(pattern,text):
        return re.search(pattern,text)
    else:
        return ''

import os
results=[]
for folder, sub_folders, files in os.walk(os.getcwd()):
    for f in files:
        if f.endswith('.txt'):#-->this is to check for only files with .txt ending
            fullpath = fullpath=folder+'/'+f
            results.append(search(fullpath))

for r in results:
    if r!='':
        print(r.group())
    