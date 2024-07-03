keys = list(input("Please Enter keys for dictionary: "))
input_string = str(input("Enter a list of numbers: "))
values = []
for number in input_string:
    values.append(int(number))

data = dict(zip(keys, values))
popped_element = data.pop("c")

print(data)
