
logo=('''
 _____________________
|  _________________  |
| |      hey!       | |
| |_____Enter!______| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
''')

def sum(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2 

def divide(n1,n2):
    if n2==0:
        return "Error:Can't divide by zero! "
    else:
        return n1 / n2
    
operation ={"+":sum, "-":subtract, "*": multiply, "/": divide,}
# print(operation["*"](4,8))
def calculator():
    print(logo)
    should_continue = True
    f_number= float(input("Enter first number: "))
    while should_continue:
        
        for sym in operation:
            print(sym)
        operator= input("Pick a mathematical operator :")

        s_number= float(input("Enter second number: "))
        answer= operation[operator](f_number,s_number)
        print(f"{f_number} {operator} {s_number} = {answer}")
        previous= input(f"Type 'y' to continue with {answer} and 'n' for new calculation: ")
        if previous== "y":
            f_number=answer
        else:
            should_continue= False
            print("\n" * 20)
            calculator()
calculator()