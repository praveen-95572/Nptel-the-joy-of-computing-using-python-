from PIL import Image
im=Image.open('test1.png')
rgb_im=im.convert('RGB')
r,g,b=rgb_im.getpixel((150,2))
print(r,g,b)
