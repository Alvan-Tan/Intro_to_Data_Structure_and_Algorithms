items = ["apple", "pear", "orange", "banana", "watermelon",
         "apple", "pear", "orange", "banana", "watermelon",
         "apple", "pear", "orange", "banana", "watermelon"]

unique_fruits = {}

for item in items:
    unique_fruits[item] = 0

result = set(unique_fruits.keys())
print(result)
