numbers = list()
n = int(input("Please Enter how many items you need in the list: "))
for i in range(0, n):
    items = int(input("Please enter a number: "))
    numbers.append(items)

p = int(input("Please Enter a number to check if it's there in list: "))

# 1 2 3
# 2
# item = 1, target = 2  --> flag = 0
# item = 2 , target = 2 --> flag = 1
# item = 3 , target = 2 --> flag = 0

flag = False
for item in numbers:
    if p == item:
        flag = True
        break


if flag:
    print("{0} is present in the list".format(p))
else:
    print("{0} is not present in the list".format(p))
