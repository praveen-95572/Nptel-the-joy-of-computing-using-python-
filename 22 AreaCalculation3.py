import numpy as np
from PIL import Image
import scipy.misc
import random

img=scipy.misc.imread("map-01.png")
count_pun=0
count_in=0
count=0

while(count<=10000):
     x=random.randint(0,2735)
     y=random.randint(0,2480)
     z=0
     if(img[x][y][z]==60):
          count_in+=1
          count+=1
     else:
          if(img[x][y][z]==80):
               count_pun+=1
               count+=1
area_pun=(count_pun/count_in)*3287263
print("Area of Punjab = ",area_pun)
