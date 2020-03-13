# fibonacci series by using recurrsion.
def fibonacci(num):
    if (num==1 or num==2):
        return 1
    else:
        return fibonacci(num-1)+fibonacci(num-2)
number=10
for x in range(number):
    print(fibonacci(x+1))       


# we can find out fibonacci series by without using recurrsion way too.

'''num=11
fib_list=[]
def fib(num):
    if (num==0 or num==1):
        fib_list.append(1)
    else:
        fib_list.append(fib_list[num-1]+fib_list[num-2])
    return fib_list 
for x in range(num):
    fib(x)
for x in fib_list:
    print(x)  ''' 



    
