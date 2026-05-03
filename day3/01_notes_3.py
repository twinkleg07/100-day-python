#---Even/Odd---
# n= int(input("Enter a number to check even or odd"))
# if n % 2 == 0:
#     print("The number is even")
# else:
#     print("The number is odd")          #(command+z to undo)


#---rollercoaster---
print("Welcome to roller coaster")
height= int(input("What is your height in cm?"))
bill = 0
if height >= 120:
    age = int(input("What is your age?"))
    if age <= 12:
        bill=50
        print("You have to pay 50 rupees")
    elif age <= 18:
        bill = 70
        print("You have to pay 70 rupees")
    else:
        bill=100
        print("You have to pay 100 rupees") 
    photo= input("Do you want to have photo? Type y for yes n for no. ")
    if photo == "y":
        bill += 20
    print("Your bill is ", bill)
else :
    print("You can't ride the roller coaster")


#---bgmi---
# weight = 85
# height = 1.85

# bmi = weight / (height ** 2)

# # 🚨 Do not modify the values above
# # Write your code below 👇
# if bmi < 18.5:
#     print("underweight")
# elif bmi < 25:
#     print("normal weight")
# else:
#     print("overweight")


