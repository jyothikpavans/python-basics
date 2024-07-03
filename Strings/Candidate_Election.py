candidates = str(input("Enter names of candidates: "))
candidates_list = []
for candidate in candidates.split(" "):
    candidates_list.append(candidate)

candidates_dict = {}
maximum = 1
count = 1
for candidate in candidates_list:
    if candidate in candidates_dict:
        candidates_dict[candidate] += 1
        if candidates_dict[candidate] > maximum:
            maximum = candidates_dict[candidate]
    else:
        candidates_dict[candidate] = 1

print(candidates_dict)
print(maximum)
winner_list = []
for key in candidates_dict:
    if candidates_dict[key] == maximum:
        winner_list.append(key)

print(sorted(winner_list)[0])


