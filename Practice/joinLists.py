letters = ["a","b","c"]
numbers = [1,2,3]

letters.extend(numbers)

print(letters)

for x in letters:
    numbers.append(x)

print(numbers)


