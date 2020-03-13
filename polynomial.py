print("WELCOME TO POLYNOMIAL PROGRAM")
poly=input("Enter the any linear polynomial expression:y=")

if poly[0]=="-" and poly[3]=="+":
    a=int(poly[1])
    a=-a
    b=int(poly[4])
    print("cool 1")
elif poly[2]=="-" :
    a=int(poly[0])
    b=int(poly[3])
    b=-b
    print("cool 2")
elif poly[0]=="-" and poly[3]=="-":
    a=int(poly[1])
    a=-a
    b=int(poly[4])
    b=-b
    print("cool 3")
else:    
  a=int(poly[0])
  b=int(poly[3])
  print("cool 4")
###################################################
x=input("Enter the value of x:")
x=int(x)
print(x+2)
y=(a*x)+b
print("y:"+str(y))
print("coordinate:("+str(x)+","+str(y)+")")

