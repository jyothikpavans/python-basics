input_keys = str(input("Please Enter keys for dictionary: "))
input_values = str(input("Enter a list of numbers: "))
keys = []
values = []
for key in input_keys.split(" "):
    keys.append(key)
for value in input_values.split(" "):
    values.append(int(value))

data = dict(zip(keys, values))
sum_items = 0
for key in data.keys():
    sum_items += data[key]

print(sum_items)

