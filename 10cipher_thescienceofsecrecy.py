import string
dict={}
data=" "
file=open("op_file.txt","w")
for i in range(len(string.ascii_letters)):
     dict[string.ascii_letters[i]]=string.ascii_letters[i-2]
print(dict)

with open("ip_file.txt") as f:                     
     while True:
          c=f.read(1)
          if not c:
               print("\n End of File . ")
               break
          if c in dict:
               data=dict[c]
          else:
               data=c
          print(data)
          file.write(data)

file.close()
