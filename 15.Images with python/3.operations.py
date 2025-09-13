from PIL import Image
mac=Image.open('pencils.jpg')
print(mac.size)
x=0
y=0
w=1950*0.5
h=1300*0.5
croped_mac=mac.crop((x,y,w,h))
croped_mac.show()

mac=Image.open('example.jpg')
print(mac.size)
half_way=1993/2
x=half_way-200
w=half_way+200
y=800
h=1257
croped_mac=mac.crop((x,y,w,h))
mac.paste(im=croped_mac,box=(0,0))
rotated_mac=mac.rotate(90)
rotated_mac.show()
resized_mac=mac.resize((1280,400))
resized_mac.show()
