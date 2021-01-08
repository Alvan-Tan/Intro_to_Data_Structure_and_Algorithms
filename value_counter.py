items = ["apple", "pear", "orange", "banana", "watermelon",
         "apple", "pear", "orange", "banana", "watermelon",
         "apple", "pear", "orange", "banana", "watermelon"]

unique_fruits = {}

for item in items:
    if item in unique_fruits.keys():
        unique_fruits[item] += 1
    else:
        unique_fruits[item] = 1

print(unique_fruits)
