n = int(input("Please Enter no of units of current used: "))
if 1 <= n <= 100:
    cost_unit_below100 = 10
    price = n * cost_unit_below100
elif 101 <= n <= 200:
    cost_unit_below200 = 15
    price = 100 * 10 + (n - 100) * cost_unit_below200
elif 201 <= n <= 300:
    cost_unit_below300 = 20
    price = 100 * 10 + 100 * 15 + (n - 200) * cost_unit_below300
else:
    cost_unit_above300 = 25
    price = 100 * 10 + 100 * 15 + 100 * 20 + (n - 300) * cost_unit_above300

print(price)
