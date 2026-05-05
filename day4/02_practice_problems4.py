import random 
#---Random heads or tails---
random_head_or_tail = random.randint(1,2)
if random_head_or_tail == 1:
    print("Heads")
else:
    print("tails")

# ---Name Shuffle game--- 
friends =["Alice", "Bob", "Charlie", "David", "Emanuel"]
friend_no = random.randint(0,4)
print(friends[friend_no])
#or
print(random.choice(friends))