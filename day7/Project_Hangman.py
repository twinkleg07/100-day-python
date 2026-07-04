import random 

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = [
    "aardvark",
    "baboon",
    "camel",
    "python",
    "apple",
    "banana",
    "orange",
    "computer",
    "science",
    "keyboard",
    "programming",
    "coffee",
    "football",
    "mountain",
    "ocean"
]
print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
''')
word= random.choice(word_list)
print(word) 

lives = 6

placeholder= ""

for i in range(len(word)):
    placeholder += "_ "
print(placeholder)

project_end= False

list=[]

while project_end== False:
    print(f"------{lives}/6 lives left------")

    guess = input("Guess a letter: ").lower()
    print(guess)

    if guess not in word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word.\nYou lose a life.")
    
    if guess in list:
        print("----You have already guessed it!----")

    display =""

    for letter in word:
        if letter == guess :
            display+= letter
            list.append(letter)
        elif letter in list:
            display += letter
        else:
            display+="_"

    print(display)

    if "_" not in display:
        project_end = True
        print("------You win!------")
    elif lives == 0:
        project_end = True
        print(f"------You Lose!------\nThe word was ***{word}***")

    print(stages[lives])

