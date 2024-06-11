# remove() - removes a specified item from the list

vegetables = ['lettuce','mint','cabbage','brookly']
print(vegetables)
vegetables.remove('brookly')
print("Vegetables include",vegetables, "\n")

print("\n")
print("\n")
# pop() - removes the specified index
clothes = ['pants','sweaters','shirts']
print(clothes)
clothes.pop(0)
print(clothes)

print("\n")
print("\n")
#del also removes the specified index or the list
shoes = ['sneakers','sandals','slippers']
print(shoes)
del shoes[1]  # removes slippers from the list
print(shoes)

del shoes     # removes the entire list


print("\n")
print("\n")
# clear() empties the entire list
junk_food = ['hamburger','pizza']
print(junk_food)

junk_food.clear()
print(junk_food)
