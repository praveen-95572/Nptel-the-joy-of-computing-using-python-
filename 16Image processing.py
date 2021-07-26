
from PIL import Image
img=Image.open('obtained.png')          #opening the image
#Transposing
transposed_img=img.transpose(Image.FLIP_LEFT_RIGHT)
transposed_img.save('corrected_img.png')
print("Done Flipping")


import cv2
img=cv2.imread('crime.png')

#Preparing CLAHE

clahe=cv2.createCLAHE()
    #convert to gray scale image
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    #apply enhancement
ench_img=clahe.apply(gray_img)
cv2.imwrite('enhanced.png',ench_img)
print("Done Enhancing")
