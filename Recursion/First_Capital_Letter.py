def first_capital_letter(index) -> str:
    if index == len(string):
        return ""
    if 65 <= ord(string[index]) <= 90:
        return string[index]
    return first_capital_letter(index + 1)


string = str(input("Enter a string: "))
index = 0
if first_capital_letter(index) == "":
    print("No capital letter found")
else:
    print(first_capital_letter(index))
