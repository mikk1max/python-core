# print("Hello world!")

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


# def factorial(n):
#     if n < 2:
#         return 1
#     else:
#         return n * factorial(n - 1)

# def number_of_groups(n, k):
#     return int(factorial(n) / (factorial(n - k) * factorial(k)))

# print(number_of_groups(1, 4))


# from datetime import datetime

# current_datetime = datetime.now()
# print(current_datetime.tzinfo)


# with open("test.txt", "w") as fh:
#     fh.write("first line\nsecond line\nthird line")

# with open("test.txt", "r") as fh:
#     lines = [el.strip() for el in fh.readlines()]

# print(lines)

# byte_str = "some text".encode()
# print(byte_str)


# from jokes import get_random_joke


# def main():
#     name = input("Please, write your name: ")
#     print(f"Hi, {name}!")

#     while True:
#         user_response = input(f"{name}, do you want a joke? (yes/no): ").lower()
#         if user_response == "yes":
#             print(get_random_joke())
#         elif user_response == "no":
#             print(f"Goodbye, {name}!")
#             break


# if __name__ == "__main__":
#     main()


# import math
# from venv_test.log import log_info, log_warning, log_error


# def calculate_square_root(numbers: list) -> None:
#     for number in numbers:
#         try:
#             if number < 0:
#                 log_warning(f"Знайдено від'ємне число: {number}. Пропускаємо.")
#                 continue

#             root = math.sqrt(number)
#             log_info(f"Квадратний корінь з {number} - {root:.2f}")

#         except Exception as e:
#             log_error(f"Помилка при обчисленні кореня для {number}: {e}")


# if __name__ == "__main__":
#     numbers = [16, -4, 9, 25, 0, 4, "16"]
#     calculate_square_root(numbers)


from temperature_stats.data import load_data, clean_data
from temperature_stats.processing import calculate_statistics


def main():
    filename = "temperature_stats/temperatures.txt"
    raw_data = load_data(filename)
    temperatures = clean_data(raw_data)
    stats = calculate_statistics(temperatures)

    if stats:
        print(f"Minimum Temperature: {stats['min']}°C")
        print(f"Maximum Temperature: {stats['max']}°C")
        print(f"Average Temperature: {stats['average']:.2f}°C")
        print(f"Median Temperature: {stats['median']:.2f}°C")
    else:
        print("No temperature data available.")


if __name__ == "__main__":
    main()
