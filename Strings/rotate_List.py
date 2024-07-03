input_string = str(input("Enter a list of numbers: "))
rotate_list = []
for number in input_string.split(" "):
    rotate_list.append(int(number))

no_rotations = int(input("Enter no of rotations: ")) % len(rotate_list)
first_index = 0
last_index = len(rotate_list) - 1

for rotation in range(no_rotations):
    rotate_list.append(rotate_list[first_index])
    rotate_list.remove(rotate_list[first_index])
print(rotate_list)
