n = int(input("Please Enter a number: "))
strings = "289"
new_string = ""
another_new_string = ""
for i in range(2, 0, -1):
    new_string += strings[len(strings) - i]
print(new_string)

for k in range(0, 1):
    another_new_string += strings[k]
print(another_new_string)

if int(new_string) + int(another_new_string) == n:
    print("YES YES YES")

