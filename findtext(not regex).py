import module
text=input()
for x in range(len(text)):
    t=text[x:x+12]
    if module.findtext(t):
        print("text found:"+t)
print("done")        