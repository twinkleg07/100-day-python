student_score = [ 180,124, 165, 173,189,169,146]
# sum(student_score) code below to show how sum() works
sum=0
for score in student_score:
    sum += score
print(sum)

# # max(student_score) code below to show how max() works
maxi=0
for score in student_score:
    if score>maxi:
        maxi=score
print(maxi)


#---FizzBuzz--- (number divisible by 3=Fizz,5=Buzz,Both=FizzBuzz)
for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0:
        print("Fizz")
    else:
        print(num)