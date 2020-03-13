# this is pthon prgram for finding the word and then replace this word by other word 
import pyperclip,re
finding_word=input("Enter the finding word :")     # this is finding word
replacing_word=input("Enter the replacing word :")  # this is replacing word
long_text=str(pyperclip.paste())                # this is long text from which all changes happen
word_regex=re.compile(finding_word)
mo=word_regex.findall(long_text)
print("words comes",str(len(mo)),"times in this long text")
new_longtext=word_regex.sub(replacing_word,long_text)    # this is new long text
pyperclip.copy(new_longtext)