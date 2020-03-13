# This is python program to find reverse string of given string.

string_value="string"
print(string_value)

# this is function which reverse the string.
def reverse_string(string):
    reverse_list=[]
    for x in range(len(string)):
        reverse_list.append(string[-(x+1)])
    return "".join(reverse_list)
rev_string=reverse_string(string_value)   
print(rev_string) 