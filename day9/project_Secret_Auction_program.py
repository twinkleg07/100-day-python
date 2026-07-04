print('''

                     ___________
                     \         /
                      )_______(
                      |"""""""|_.-._,.---------.,_.-._
                      |       | | |               | | ''-.
                      |       |_| |_             _| |_..-'
                      |_______| '-' `'---------'` '-'
                      )"""""""(
                     /_________|
                    /''-------''|
                   /-------------|
                  /_______________|
''')
def hightes_bid(dictionary):
    winner=""
    highest=0
    for bidder in dictionary:
        bid_amount= dictionary[bidder]
        if bid_amount>highest:
            hightest=bid_amount
            winner=bidder
    print("\n"*20)
    print(f"Winner is {winner} with a bid of {highest}.")

d={}

continue_loop= True
while continue_loop:
    name= input("What is your name?: ")
    bid= int(input("What is your bid?: $"))
    d[name]= bid 
    other_user= input("Is there other users who wants to bid? type yes/no: ").lower()
    if other_user== "no":
        continue_loop= False
        hightes_bid(d)
    elif other_user== "yes":
        print("\n"*20)
        

