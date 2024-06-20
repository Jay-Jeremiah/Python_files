#functions - block of code used to run a specific instruction

num1 = 23

num2 = 24

total = num1 + num2

print("The total is ",total)


# to perform the above tasks, we can write them in a function
# denoted by def keyword 

def addition(figure1,figure2):
    add = figure1 + figure2
    return add

figure3 = int(input("Enter number A: "))
figure4 = int(input("Enter number B: "))


#calling the function
summation = addition(figure3,figure4)
print(summation)