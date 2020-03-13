
# this is python program thgrouh which we can find any word in long text and 
# also that how many times this word comes.

string=input("Enter the long text:")
find_word=input("Enter the finding word:" )
string_length=len(string)
length=len(find_word)
count=0
for x in range(string_length):
    if string[x:x+length]==find_word:
        print(string[x:x+length])
        count+=1
print("count",count)        

