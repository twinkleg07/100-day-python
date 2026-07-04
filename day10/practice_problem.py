def is_leap_year(year):
    """Tells if the entered year is leap year or not"""
    if year % 4 == 0:
        if year % 100==0:
            if year % 400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

print(is_leap_year(int(input("Enter a year to check if its leap year or not: "))))