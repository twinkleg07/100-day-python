def format_name(f_name,l_name):
    """Take first and last name and format it to return to title case version""" #Docstring
    if f_name=="" or l_name=="":
        return "You didn't provide input"
    
    formatted_f= f_name.title()
    formatted_l= l_name.title()
    return f"{formatted_f} {formatted_l}"
    
f_name= input("Enter your first name: ")
l_name= input("Enter your last name: ")
print(format_name(f_name,l_name))