# def fibonacci_series_up_to_n_elements(number, last_term, last_before_term, original_number):
#     if number > original_number:
#         return
#     if number == 1:
#         print(n_minus2)
#     if number == 2 or number == 3:
#         print(n_minus1)
#     if 2 < number < original_number:
#         print(last_term)
#     fibonacci_series_up_to_n_elements(number + 1, last_term + last_before_term, last_term, original_number)

def fibonacci_series_up_to_n_elements(number, last_term, last_before_term, original_number):
    if number > original_number:
        return
    if number == 1:
        print(n_minus2)
    if number == 2 or number == 3:
        print(n_minus1)
    if 2 < number < original_number:
        print(last_term)
    fibonacci_series_up_to_n_elements(number + 1, last_term + last_before_term, last_term, original_number)


n = int(input("Enter a number: "))
n_minus1 = 1
n_minus2 = 0
number = 1
original_number = n
fibonacci_series_up_to_n_elements(number, n_minus1, n_minus2, original_number)
