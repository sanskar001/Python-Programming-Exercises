count=0
string=input("Enter the string:")
letter=input("Enter the letter which you want to find out:")
for x in string:
    if letter==x:
       count+=1
print("number of  that letter in given string:"+ str(count)) 
print("Thankyou")      