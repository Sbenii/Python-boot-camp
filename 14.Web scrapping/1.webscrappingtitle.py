import requests
result=requests.get("https://www.example.com/")

print(type(result))
print(result.text)

import bs4
soup=bs4.BeautifulSoup(result.text,'lxml')
print(soup)
print(soup.select('title')[0].getText())
site_paragraphs=soup.select('p')
print(site_paragraphs[0].getText())