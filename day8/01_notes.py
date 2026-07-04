def greet(n,age):
    print(f"Hello {n}")
    print(f"You are {age} years old")
    print("Welcome to greet box")

greet("twinkle",19)
greet(age=18,n="twinkle")
# parameter= n (name) argument= twinkle (value)

#Inspired by article by Tim Urban - Your Life in Weeks and 
          # realised just how little time we actually have.
def life_in_weeks(age):
    weeks= age*52
    total= 90*52
    left= total-weeks
    print(f"You have {left} weeks left.")
    
life_in_weeks(19)
