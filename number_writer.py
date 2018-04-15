import json

numbers_1 = [1, 5, 3, 6, 2, 4, 7]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers_1, f_obj)

with open(filename) as f_obj:
    numbers = json.load(f_obj)
print(numbers)

