import random
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
def deal_card() :
    user= random.choices(cards,k=2)
    computer= random.choices(cards,k=2)

    user_sum=sum(user)
    csum=sum(computer)
    print(f"Your Cards: {user}, current score {user_sum}")
    print(f"Computer's first Cards: {computer[0]}")
    another_card=input("Type'y' to get another card, type'n'to pass: ").lower()
    y= True
    while y:
        if user_sum==21:
            print("You win! You have a Blackjack 🥳")
            break
        elif csum==21:
            print("You lose! Opponent has a Blackjack 😱")
            break
        if user_sum > 21:
            print("You lose! Sum is over 21!😭")
            break
        elif csum > 21:
            print("You Win! Opponent's sum is greater than 21!")
            break
        if user_sum > 21 and 11 in user:
            user_sum -= 10


        elif csum<21 and user_sum<21:
            if user_sum>csum:
                print("You Win!Your sum is higher!🥳")
                break
            elif user_sum<csum:
                print("You lose! Opponent's sum is higher!😱")
                break
            elif user_sum==csum:
                print("Its's a draw! 😳")
                break

        if another_card=="n":
            y=False
            print(f"Your final hand: {user}, final score: {user_sum}")
        elif another_card=="y":
            while another_card=="y":
                user.append(random.choice(cards))
                user_sum=sum(user)
                print(f"Your cards: {user}, current score: {user_sum}")
                another_card=input("Would you like another card? Type 'y' for card, Type'n'to pass: ").lower()

        while csum<17:
            computer.append(random.choice(cards))
            csum= sum(computer)
            if user_sum >= 21:
                break



deal_card()
