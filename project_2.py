# this python program to finding out email address from long string
# example654@gmail.com

import re
import test
email_regex=re.compile(r'(\w+)(@)(gmail|yahoo)(.com)')
match_object=email_regex.findall('''these are email address of all students came here for summer taining program 
snaskarm001@gmail.com,
abhishek@yahoo.com,
manasbhamu345@gmail.com,
kardamsoni7857@yahoo.com,
muditagrawalyoyo00432@gmail.com
thankyou
thats all!!!!!!!''')
for x in match_object:
    test.tuple_to_string(x)

# in module test function is 
'''def tuple_to_string(tuple_name):
    list_name=list(tuple_name)
    print("".join(list_name))
   '''    