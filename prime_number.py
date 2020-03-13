# This is python program to find number is prime or not prime.

def prime(number):    # function of finding prime number
    flag=0            # flag variable for just indicating purpose
    if number>0:
        for x in range(2,number):
            if number%x==0:
                flag=1
                return False
                break
        if flag==0:
            return True

# this is function to find the prime numbers between the lowest and highest number.

def prime_series(lowest_number,highest_number):
    count=0
    prime_list=[]
    for x in range(lowest_number,highest_number+1):
        if prime(x)==True:
            prime_list.append(str(x))
            count=count+1
    print(count,"prime numbers exist between",lowest_number,"and",highest_number,":")
    print(" ".join(prime_list))


prime_series(-10,50)    

# this is another way finding the prime number by using while lopp.
'''
def prime(number)
    i=2
    toggle=0
    while i<number:
        if number%i==0:
            toggle=1
            print("number is not prime.")
        i=i+1
    if toggle==0:
        print("number is prime")
        '''