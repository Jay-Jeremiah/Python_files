#if/else are conditional statements
#if the if condition is met, the else condition is skipped from execution
# if the if condition is not met, the else condition is executed.

number = 10

if number >= 0:
    print("It is a positive number.")
else:
    print("It's a negative number.")

name = ['Harry','Ryan']
name1 = input("What is your name?: ")

if name1 in name:
    print("You are a student")
else:
    print('You are not a student.')