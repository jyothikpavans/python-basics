# list = [1,2,3,1]
# dict = {}.fromkeys(list)
# print(dict)
def beautifulBinaryString(b):
    # Write your code here
    minimum_moves = 0
    n = len(b)
    index = 0
    for value in b:
        if b[index] == 0:
            if (b[index + 1] == 1) and (b[index + 2] == 0):
                minimum_moves = minimum_moves + 1
                b[index + 2] = 1
        index += 1

    return minimum_moves


binary = str(input("Enter a binary string: "))
print(beautifulBinaryString(binary))
