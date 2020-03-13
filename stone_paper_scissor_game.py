# This is python program to make "stone paper scissor" game.
import random   # importing random module.

p1_name = input("Enter the first person name:")
p2_name = input("Enter the second person name:")  
import random

first_name = ["Jake","Mike","Kate","Henry","Schotty","Gimmy","Charles","Black","Karlie","Timmy"]

last_name = ["smith","doe","jankens","robinson","davis","jaffarson","jacob","wright","peterson","micheal"]

street_name = ["Main","High","Pearl","Maple","Park","Pine","Oak","kadle","Elm"]

fake_cities = ["Metroplois","Eerie","King's landing","Sunnydale","Bedrock","South park","Atlantis"]

States = ["AK","AL","AR","AZ","CA","CO","CT","DC","DE"]

for n in range(20):
    f_name = random.choice(first_name)
    l_name = random.choice(last_name)

    phone_number = f"{random.randint(100,999)}-555-{random.randint(1000,9999)}"

    street_number = random.randint(100,999)

    street = random.choice(street_name)

    city = random.choice(fake_cities)
    state = random.choice(States)
    zipcode = random.randint(10000,99999)

    address = f"{street_number} {street} St., {city} {state} {zipcode}"

    email = f"{f_name.lower()}{l_name.lower()}@gmail.com"

    print(f"name: {f_name} {l_name}")
    print(f"Phone number: {phone_number}")
    print(f"Address: {address}")
    print(f"Email address: {email}")
    print("--------------------------------")
 #input("Enter the second person name:")

game_choice = ["stone","paper","scissor"]

p1_score = 0 
p2_score = 0

for n in range(3):
    p1_input = random.choice(game_choice)
    p2_input = random.choice(game_choice)
    print(f"{p1_name} choice is: {p1_input} ")
    print(f"{p2_name} choice is: {p2_input} ")

    if(p1_input == "stone" and p2_input =="scissor") or (p1_input == "paper" and p2_input == "stone") or (p1_input == "scissor" and p2_input == "paper"):
        p1_score  = p1_score + 1
    elif(p2_input == "stone" and p1_input =="scissor") or (p2_input == "paper" and p1_input == "stone") or (p2_input == "scissor" and p1_input == "paper"):
        p2_score = p2_score + 1

    print(f"{p1_name} score is: {p1_score}           {p2_name} score is: {p2_score}")    
    print("------------------------------------------")

print(f"{p1_name} total score is {p1_score}")
print(f"{p2_name} total score is {p2_score}")
print("--------------")
if p1_score > p2_score:
    print(f"{p1_name} win")
elif p1_score < p2_score:
    print(f"{p2_name} win")
else:
    print(f"game is draw between {p1_name} and {p2_name}")
