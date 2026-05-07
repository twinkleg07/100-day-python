import random 
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j","k", "l", 
           "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers= ["1","2","3","4","5","6","7","8","9"]
symbols =["!","#","$","%","&","(",")","*","+"]

print("Welcome to the Password Generator!")
nr_letters = int(input("How many letters would you like in your password\n?"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

#---Easy version---
# password = ""

# for char in range(0,nr_letters):
#     r=random.choice(letters)
#     password+= r

# for char in range(0,nr_symbols):
#     s=random.choice(symbols)
#     password += s

# for char in range(0,nr_numbers):
#     n=random.choice(numbers)
#     password+= n

# print(password)

#---Actual code---
password_l = []

for char in range(0,nr_letters):
    password_l.append(random.choice(letters))

for char in range(0,nr_symbols):
    password_l.append(random.choice(symbols))
  
for char in range(0,nr_numbers):
    password_l.append(random.choice(numbers))
    
random.shuffle(password_l)
print(password_l)

password=""
for char in password_l:
    password += char

print(password)
