import random 
scissor=''' 
    .-.  _
    | | / )
    | |/ /
   _|__ /_
  / __)-' )
  \  `(.-')
   > ._>-'
  / \/
      '''

paper=''' 
          ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----'          '''

rock='''
       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"'''

computer=[rock,paper,scissor]

choice= int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors"))
if choice>=0 and choice<=2:
    print(computer[choice])

computer_choice=random.randint(0,2)
print("Computer choose: ")
print(computer[computer_choice])

if choice>=3 or choice<0:
    print("Incorrect Input. You lost!")
elif choice==0 and computer_choice==2:
    print("You win!")
elif computer_choice==0 and choice==2:
    print("You Lost!")
elif choice > computer_choice:
    print("You win!")
elif computer_choice>choice:
    print("You lost!")
elif choice==computer_choice:
    print("It's a draw!")
