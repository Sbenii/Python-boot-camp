#Get a title of a book with a two star rating on books.toscrape.com
import requests
import bs4
base_url='https://books.toscrape.com/catalogue/page-{}.html'
page_number=12
print(base_url.format(page_number))

'''
example=products[0]
print(example.select('.star-rating.Three'))
print(example.select('a'))
print(example.select('a')[1])
print(example.select('a')[1]['title'])
'''

#Final deliverables
two_star_titles=[]

for x in range(1,51):
    page_number=x
    res=requests.get(base_url.format(page_number))
    soup=bs4.BeautifulSoup(res.text,'lxml')
    products=(soup.select('.product_pod'))
    for n in range(0,20):
     example=products[n]
     if example.select('.star-rating.Two'):
         two_star_titles.append(example.select('a')[1]['title'])
     else:
         continue
     
print('Products with a two star rating:',two_star_titles)
