import requests
import bs4
page_still_valid=True
authors=[]
page=1
base_url='https://quotes.toscrape.com/page/{}'
while page_still_valid:
    res=requests.get(base_url.format(page))
    if 'No quotes found!' in res.text:
        break
    soup=bs4.BeautifulSoup(res.text,'lxml')
    for item in soup.select('.author'):
        authors.append(item.text)
    page+=1

Authors_unique=set(authors)
Final_list_of_unique_authors=list(Authors_unique)

for item in range (len(Final_list_of_unique_authors)):
    print(f'Author{item+1}: {Final_list_of_unique_authors[item]}')