#when having two conditions that have to be met, we can use if and elif

fruits = ['Apples','Pineapples','Oranges']

name = input('What is your favourite fruit?:  ')

if name == 'Bananas':
    print('Congratulations!')
elif name in fruits:
    print(f"You win 2{name}")
else:
    print('Try next time')