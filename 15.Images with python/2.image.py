from  PIL import Image

mac=Image.open('example.jpg')
mac.show()
print(mac.size)
print(mac.filename)
print(mac.format)