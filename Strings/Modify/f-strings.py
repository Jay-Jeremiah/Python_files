# f-strings help us to combine numbers and strings in the line of code

age = 19

a = f"My name is Harry, I am {age} years"

print(a)

 # f-strings are indicated by f infront of the string 
 # and {} on the variable


# f-strings can be modified by using : followed by 
# legal writing like .2f meaning add 2 decimals

price = 56

buyer = "How much does the fridge cost"

seller = f"It costs {price:.2f} dollars"

print(buyer)
print(seller)

# they are modified by doing arithmetic operations

price1 = 56 
price2 = 78.99

buyer1 = "Thank you. May I get the total expediture please?"

seller1 = f"Your total expediture is {price1 + price2}"

print(buyer1)
print(seller1)