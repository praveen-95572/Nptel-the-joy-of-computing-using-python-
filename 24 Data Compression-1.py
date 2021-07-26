
import numpy as np
'''
a=np.array([1,2,3])
print(a)
print(type(a))
print(a.shape)
print(a[0],a[1],a[2])

a=np.array([[1,2,3],[4,5,6]])
print(a)
print(type(a))
print(a.shape)

b=np.zeros((3,3))
print(b)
b=np.ones((3,3))
print(b)
b=np.full((2,2),3)
print(b)
b=np.random.random((2,2))
print(b)

'''

x=np.array([1,2])
print(x.dtype)      #data type of element

x=np.array([1,2],dtype=np.int64)        #forcing the data type to change to int64 from  int32
print(x.dtype)

x=np.array([[1,2],[3,4]],dtype=np.float64)

y=np.array([[5,6],[7,8]],dtype=np.float64)


print("Addition  :  \n",np.add(x,y))   #print(x+y)
print("Subtraction  \n:  ",np.subtract(x,y))
print("Multiplicaion  \n:  ",np.multiply(x,y))
print("Division  \n:  ",np.divide(x,y))
print("Square root  :  \n",np.sqrt(x))
print("Transpose : \n",(x.T))
print("Sum of element of x : ",np.sum(x))
print("Sum of element of  x column-wise : ",np.sum(x,axis=0))
print("Sum of element of  x row-wise : ",np.sum(x,axis=1))
