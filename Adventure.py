available_exits = ["east", "north","west","south"]

chosen_exit = ""
while chosen_exit not in available_exits:
    chosen_exit= input("Please choose a direction: ")
    if chosen_exit.casefold() =="quit":
        print("Game over")
        break

else:
    print("aren't you glad you got out of there")
