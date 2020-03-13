# This is python program to find out the pair inside given sequence which have sum equal to given number.

def number_arrange(seq,number):
    first = []
    second = []
    for n in seq:
        if n <= number:
            first.append(n)
        else:
            second.append(n)
    
    return first + second

input_seq = [1,2,42,5,2,1,4,5,65]
print(number_arrange(input_seq,10))