# List Comprehensions
even_squares = [x**2 for x in range(1, 10) if x % 2 == 0]
print(even_squares)


# Set Comprehensions
odd_squares = {x**2 for x in range(1, 10) if x % 2 != 0}
print(odd_squares)


# Dictionary Comprehensions
sq_dict = {x: x**2 for x in range(1, 10) if x > 5}
print(sq_dict)
