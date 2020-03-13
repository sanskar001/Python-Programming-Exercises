# This is python program to find the string is palindome in nature or not.

def palindrome(string):
    length=len(string)
    count=0
    if (length%2==0):    
        print("palindome is not possible")
    else:
        for x in range(int(length/2)):
            if string[x]==string[-(x+1)]:
                count=count+1
        if count==int(length/2):
            print(string," is palindrome string.")  
        else:
            print(string," is not palindrome string.")  

palindrome("MADAM")