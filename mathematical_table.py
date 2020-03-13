# TABLE OF ANY NUMBER WHICH WE WANT
num=input("Enter the number:")
num=int(num)
a=1
for x in range(num,num*11,num):
    print(str(num),"*",str(a),"=",str(x))
    a+=1
print("Table is carry on from here...")    