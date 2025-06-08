print("Hello world!")

# name = input(f"Enter your name >>> ")

# print(f"Hello, {name}")

# s = "hello"
# print(s)
# s[0] = "H"


# my_list = []
# my_list.append(2024)
# my_list.append(3.12)
# my_list.insert(1, "Python")
# print(my_list)

# my_list = [2024, 3.12]
# some_data = ['Python']
# my_list.extend(some_data)
# my_list.insert(1, "Python")
# my_list.reverse()
# print(my_list)

# data = {}
# data.update({"year": 2024, "lang": "Python", "version": 3.12 })
# print(data)

# cat = {}
# info = {"status": "vaccinated", "breed": True}

# cat.update({"nick": "Simon", "age": 7, "characteristics": ["affectionate", "bitey"]})
# age = cat.get("age")
# cat.update(info)
# print(age)
# print(cat)




# is_true = True
# state = "Accept" if is_true else "Decline"

# data = None
# msg = data or "No data yet"



# work_experience = int(input("Enter your full work experience in years: "))

# if 1 < work_experience <= 5:
#     developer_type = "Middle"
# elif work_experience <= 1:
#     developer_type = "Junior"
# else:
#     developer_type = "Senior"


# print(developer_type)



# num = int(input("Enter the integer (0 to 100): "))
# sum = 0

# while num != 0:
#     sum += num
#     num -= 1

# print(num, sum)



# pool = 1000
# quantity = int(input("Enter the number of mailings: "))
# try:
#     chunk = int(pool / quantity)
# except ZeroDivisionError:
#     print('Divide by zero completed!')

# print(chunk)


# def discount_price(price, discount):
#     def apply_discount():
#         nonlocal price, discount
#         price = price * (1 - discount)
        

#     apply_discount()
#     return price

# print(discount_price(100, 0.5))


# def format_string(string, length):
#     print(len(string))
#     if len(string) < length:
#         number_of_spaces = (length - len(string)) // 2
#         print(number_of_spaces)
#         return " " * (number_of_spaces) + string
#     else:
#         return string

# result = format_string("abaa", 15)
# print(f"'{result}'")
# print(len(result))



# def first(size, *args):
#     return size + len(args)


# def second(size, **kwargs):
#     return size + len(kwargs)

# print(first(5, "first", "second", "third")) # Result: 8
# print(first(1, "Alex", "Boris")) # Result: 3
# print(second(3, comment_one="first", comment_two="second", comment_third="third")) # Result: 6
# print(second(10, comment_one="Alex", comment_two="Boris")) # Result: 12




def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)

def number_of_groups(n, k):
    return int(factorial(n) / (factorial(n - k) * factorial(k)))

print(number_of_groups(2, 3))