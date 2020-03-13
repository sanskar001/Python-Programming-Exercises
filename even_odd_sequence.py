# This is python program to rearrange seq into first EVEN NUMBER part and then ODD NUMBER part.

def even_to_odd(seq):
    even = []           # EVEN LIST
    odd = []            # ODD LIST

    for n in seq:
        if n % 2 == 0:          # FOR EVEN NUMBER
            even.append(n)
        else:                   # FOR ODD NUMBER
            odd.append(n)

    return even + odd           # THEN COMBINING EVEN WITH ODD LIST.

input_seq = [1,2,1,34,1,3]           # EXAMPLE SEQUENCE.


print(f"Input sequence:{input_seq}")
print(f"output sequence:{even_to_odd(input_seq)}")