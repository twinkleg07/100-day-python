#---Pizza order practice---
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? s, m or l ? ")
pepperoni= input("Do you want pepperoni on your pizza? y or n? ")
cheese= input("Do you want extra cheese on your pizza? y or n?")
bill=0
if size == "s":
    bill+= 150
elif size == "m":
    bill+= 250
elif size== "l":
    bill += 400
else:
    print("Incorrect Input")

if pepperoni == "y":
    if size =="s":
     bill += 30
    else:
     bill+= 50
if cheese == "y":
    bill += 30
print(f"Your total bill is: {bill} rupees")