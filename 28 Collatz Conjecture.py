def check(num):
     iterations=1
     while(num!=1):
          if num%2==0:
               num=int(num/2)
          else:
               num=3*num+1
          iterations+=1

     print(num,iterations)

num=int(input("Enter the number"))
check(num)
