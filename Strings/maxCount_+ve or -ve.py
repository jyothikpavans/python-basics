numbers_string = str(input("Enter few numbers in order: "))
numbers_list = []
for number in numbers_string.split(" "):
    numbers_list.append(int(number))

count_positive = 0
count_negative = 0

for index in range(len(numbers_list)):
    if numbers_list[index] > 0:
        count_positive += 1
    elif numbers_list[index] < 0:
        count_negative += 1
    else:
        continue

print(" max is", max(count_positive, count_negative))

