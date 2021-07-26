
import numpy
from PIL import Image

im=Image.open('lena.jpg')

pixelMap=im.load()
#    print(im.size)      return dimension
#     print(im.mode)     return typr i.e. RGB or other
img=Image.new(im.mode, im.size)
I=numpy.asanyarray(im)  # convert to array
print(I)
pixelNew = img.load()


'''
     2^8 -> 2^3
     2^8/2^3 = 2^5 = 32 values

     0-31 = 0
     32-63 = 1
     64-95 = 2
     96-127 = 3
     128-159 = 4
     160-191 = 5
     192-223 = 6
     224-255 = 7

'''
for i in range(img.size[0]):
     for j in range(img.size[1]):
          for k in range(3):
               
               if (pixelMap[i,j][k]>=0 and pixelMap[i,j][k]<=255):
                    pixelNew[i,j]=pixelMap[i,j][k]//32
          

img.save('lena_compressed.jpg')

J=numpy.asanyarray(Image.open('lena_compressed.jpg'))
print(J)



