import inspect



# Basic solution
def sol_basic(num):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

# My solution 1
def sol_1(num):
    if num % 3 == 0:
        print("Fizz", end="")
    if num % 5 == 0:
        print("Buzz")
    if num % 3 != 0 and num % 5 != 0:
        print(f"Number is {num}")

# My solution 1
def sol_2(num):
    match (num % 3 == 0, num % 5 == 0):
        case (True, True):
            print("FizzBuzz")
        case (True, False):
            print("Fizz")
        case (False, True):
            print("Buzz")
        case _:
            print(f"Number is {num}")

# decision = int(input("Enter a solution option (0-basic, 1-if-else, 2-match) >>> "))
try:
    num = int(input("Enter a number >>> "))
    match int(input("Enter a solution option (0-basic, 1-if-else, 2-match) >>> ")): 
        case 0:
            print("\n# Basic solution")
            print(inspect.getsource(sol_basic))
            print("Result >>> ", end="")
            sol_basic(num)
        case 1:
            print("\n# 1 solution")
            print(inspect.getsource(sol_1))
            print("Result >>> ", end="")
            sol_1(num)
        case 2:
            print("\n# 2 solution")
            print(inspect.getsource(sol_2))
            print("Result >>> ", end="")
            sol_2(num)
        case _:
            print("\n# Basic solution")
            print(inspect.getsource(sol_basic))
            print("Result >>> ", end="")
            sol_basic(num)
except: 
    print("This value (number or option) is not a number, please try again next time ;)")