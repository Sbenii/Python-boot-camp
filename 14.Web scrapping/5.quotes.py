import requests
import bs4
base_url='http://quotes.toscrape.com/page/{}/'
Authors=[]
for i in range(1,11):
    res=requests.get(base_url.format(i))
    soup=bs4.BeautifulSoup(res.text,'lxml')
    for item in soup.select('.author'):
        Authors.append(item.text)
All_unique_authors=set(Authors)
myli=list(All_unique_authors)
for item in range(len(myli)):
    print(myli[item])

    