# challenge yourself with a program that calculates the area of a rectangle or cirle
# given its dimensions

def rect(Length,Width):
    Area = Length * Width
    return Area

leng = float(input("Enter the length of the rectangle here: "))

wid = float(input("Enter the width here: "))

print("The area of the rectangle is: ",rect(leng,wid))