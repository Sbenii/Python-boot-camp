import requests
import bs4

headers = {
    "User-Agent": 
                  "Chrome/140.0.0.0"
}

url = "https://en.wikipedia.org/wiki/Grace_Hopper"
result = requests.get(url, headers=headers)

soup = bs4.BeautifulSoup(result.text, 'lxml')

for item in soup.select(".vector-toc-text"):
    print(item.text)
