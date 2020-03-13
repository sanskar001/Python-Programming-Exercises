# factorial of any number by recurrsion.
def factorial(num):
    if num<=1:
        return 1
    else:
        return num*factorial(num-1)

print(factorial(6))
        
# this is python program for factorial of number but without recurrsion.

'''
def factorial(num):
    if num<=0:
        return 1
    else:
        result=1
        for x in range(num,0,-1):
            result=result*x
        return result
print(factorial(2))  
'''
