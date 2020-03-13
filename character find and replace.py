text=input("Enter the text:")
text_length=len(text)
new_text=""
f_character=input("Enter the charcater which you want to find out in text:")
r_character=input("Enter the character which you want to replace with found character:")

for c in range(text_length):
    if text[c]==f_character:
        
        new_text=new_text+r_character
    else:
        new_text=new_text+text[c]

print("original text:","'"+text+"'")
print("new text(after replacing character):","'"+new_text+"'")    