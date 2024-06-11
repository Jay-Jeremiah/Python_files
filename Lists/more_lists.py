fruits = ['apples','mango','cherry','kiwi','banana']

newlist = []

# adding list items with a in them to newlist
for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)