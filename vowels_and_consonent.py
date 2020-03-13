# This is python program to find are vowels more than consonent inside given string.

def vowel_and_consonent(string):
    count = 0
    for s in string:
        if s in ['a','e','i','o','u','A','E','I','O','U']:   # vowel list
            count = count + 1
        
    if count < len(string) - count:
        print("MORE CONSONENT")
        print(f"Number of consonent:{len(string)-count}")
    else:
        print("MORE VOWEL")
        print(f"Number of vowel: {count}")

input_string = "english"

vowel_and_consonent(input_string)