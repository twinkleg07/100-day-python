letters = ["a", "b", "c", "d", "e", "f", "g","h", "i", "j", "k", "l", "m", "n",
    "o", "p", "q", "r", "s", "t", "u","v", "w", "x", "y", "z"]
direction= input("Type 'encode'to encrypt , type 'decode' to decrypt:\n").lower()
text=input("Type your message:\n").lower()
shift= int(input("Type the shift number:\n"))

def caesar(original_text,shift_amount):
    if direction=="encrypt":
        ciper= ""
        for letter in original_text:
            shift_position= letters.index(letter)+shift_amount
            shift_position%= len(letters)
            ciper += letters[shift_position]
        
        print(f"Here is your encoded result:{ciper}")

    elif direction=="decrypt":
        output=""
        for letter in original_text:
            shift_position= letters.index(letter)-shift_amount
            shift_position%=len(letters)
            output +=letters[shift_position]

        print(f"Here is your decrypted result:{output}")
    else:
        print("Invalid input")

caesar(original_text=text, shift_amount=shift)
