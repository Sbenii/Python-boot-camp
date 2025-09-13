from PIL import Image
blue=Image.open('blue_color.png')
red=Image.open('red_color.jpg')
blue.putalpha((128))
blue.show()
red.putalpha((128))
red.show()
red.paste(im=blue,box=(0,0))
red.save('purple.png')