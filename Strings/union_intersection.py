string_1 = str(input("Please Enter a list of numbers: "))
string_2 = str(input("Please Enter another list of numbers: "))
list_1 = []
list_2 = []
for number in string_1.split(" "):
    list_1.append(int(number))
for number in string_2.split(" "):
    list_2.append(int(number))

union_dict = {}
intersection_dict = {}
union_list = []
intersection_list = []

for number in list_1:
    union_dict[number] = True

for number in list_2:
    if number not in union_dict:
        union_dict[number] = True
    else:
        intersection_dict[number] = True

union_list = list(union_dict.keys())
intersection_list = list(intersection_dict.keys())

print("Union:", union_list)
print("Intersection:", intersection_list)
