#Get a title of a book with a two star rating on books.toscrape.com
import requests
import bs4
base_url='https://books.toscrape.com/catalogue/page-{}.html'
page_number=12
print(base_url.format(page_number))
res=requests.get(base_url.format(1))
soup=bs4.BeautifulSoup(res.text,'lxml')
print(len(soup.select('.product_pod')))
