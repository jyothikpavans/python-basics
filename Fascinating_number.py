n = int(input("Please Enter a number: "))
twice_number = n * 2
thrice_number = n * 3
numberString = "" + str(n) + str(twice_number) + str(thrice_number)

nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
all_numbers_dict = {}.fromkeys(nums, 0)

for key in numberString:
    all_numbers_dict[key] += 1

flag = 1
for key in nums:
    if key == "0":
        continue
    elif all_numbers_dict[key] != 1:
        flag = 0
        break

if flag == 1:
    print("Fascinating")
else:
    print("Not Fascinating")
