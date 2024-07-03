def push():
    n = int(input("Enter the element to be inserted into stack"))
    if len(stack) == 0:
        stack.append(n)
    else:
        stack.insert(0, n)
    print(n, "is inserted into Stack.")
    print()


def pop():
    if len(stack) == 0:
        print("STACK IS EMPTY.")
    else:
        print(stack[0], "is deleted from stack.")
        del stack[0]   #pop(0)
    print()


def display():
    if len(stack) == 0:
        print("STACK IS EMPTY.")
    else:
        print("Elements of stack are: ")
        for element in stack:
            print(element)
        print("Top of the stack is", stack[0])


stack = list()
while(1):
    print("Enter the option from below\n1-Push operation\n2-POP Operation\n3-Display\nEnter any key to Exit")
    str = input()
    if str == "1":
        print("PUSH Operation")
        push()
    elif str == "2":
        print("POP Operation")
        pop()
    elif str == "3":
        print("Display Operation")
        display()
    else:
        print("Exit the Program")
        break

