# Challenge yourself with a program that calculates the area of a rectangle or circle
# given its dimensions(use input() to get the values

def rect(length,width):
    Area = length * width
    return Area

def circ(pi,rad):
    Prod = 2*pi*rad
    return Prod

print("Welcome to my program")
print("It can specifically calculate the area of a rectangle or a circle.")
print("Please choose one of the shapes below: ")

a = "Rectangle"
b = "Circle"

print(a)
print(b)

Response = input("Enter your response here: ")

if Response == a:
    leng = float(input("Enter the length here: "))
    wid = float(input("Enter the width here: "))
    print("The area of the rectangle is: ", rect(leng,wid))
elif Response == b:
    pi = 3.14
    radius = float(input("Enter the raduis of the circle: "))
    print("The area of the circle: ", circ(pi,radius))
else:
    print("Incorrect shape")
    print("You may have to try again")