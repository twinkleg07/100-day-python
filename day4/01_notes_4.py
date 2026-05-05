# In this lesson- Randomization, lists, and more
# python uses Mersenne Twister to create or generate Psedo Random Number
import random             # Module in python
r_integer= random.randint(1,10)      # for integer (from 1 , to 10) including 1 and 10
# print(r_integer)

random_no_0_to_1 = random.random()*10    # for floating point no (greater than or equal to 0, less than 1)(0 to 10 when *10)that means (>=0,<10)
# print(random_no_0_to_1)

random_float = random.uniform(1,10)       # to print(greaterthan= a, lessthan= b)
# print(random_float)

#---Random heads or tails---
random_head_or_tail = random.randint(1,2)
if random_head_or_tail == 1:
    print("Heads")
else:
    print("tails")

#---Lists---[]
states_of_india=["Hp","Hr","Bihar","Up"]
states_of_india[1]= "uk"
states_of_india.append("hr")
states_of_india.extend(["kerala","mp"])
print(states_of_india)
# index error print(states_of_india[8])

# dirty_dozen= ["Strawberry","Spinach","kale","nectarines", "Apples","Grapes","tomatoes"]
fruits= ["Strawberry","nectarines", "Apples","Grapes"]
vegetables=["Spinach","kale","tomatoes"]
dirty_dozen=[fruits,vegetables]         #Nested list
print(dirty_dozen[0][1])