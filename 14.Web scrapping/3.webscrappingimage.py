import requests
import bs4

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/140.0.0.0 Safari/537.36"
}
result=requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)",headers=headers)
soup=bs4.BeautifulSoup(result.text,'lxml')
computer=soup.select('.mw-file-element')[1]
print(computer['class'])
print(computer['src'])

image_link=requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/250px-Deep_Blue.',headers=headers)
print(image_link.content)

f=open('My computer_image.jpg','wb')
f.write(image_link.content)

f.close()