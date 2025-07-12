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


# from temperature_stats.data import load_data, clean_data
# from temperature_stats.processing import calculate_statistics


# def main():
#     filename = "temperature_stats/temperatures.txt"
#     raw_data = load_data(filename)
#     temperatures = clean_data(raw_data)
#     stats = calculate_statistics(temperatures)

#     if stats:
#         print(f"Minimum Temperature: {stats['min']}°C")
#         print(f"Maximum Temperature: {stats['max']}°C")
#         print(f"Average Temperature: {stats['average']:.2f}°C")
#         print(f"Median Temperature: {stats['median']:.2f}°C")
#     else:
#         print("No temperature data available.")


# if __name__ == "__main__":
#     main()


# class Animal:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight

#     def say(self):
#         pass

#     def change_weight(self, weight):
#         self.weight = weight


# class Owner:
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address

#     def info(self):
#         return {"name": self.name, "age": self.age, "address": self.address}


# class Dog(Animal):
#     def __init__(self, nickname, weight, breed, owner: Owner):
#         self.breed = breed
#         self.owner = owner

#         super().__init__(nickname, weight)

#     def say(self):
#         return "Woof"

#     def who_is_owner(self):
#         return self.owner.info()


# owner = Owner("Sherlock", 24, "London, 221B Baker Street")
# dog = Dog("Simon", 10, "british", owner)
# print(dog.who_is_owner())


# class Animal:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight

#     def say(self):
#         pass


# class Cat(Animal):
#     def say(self):
#         return "Meow"


# class Dog(Animal):
#     def say(self):
#         return "Woof"


# class CatDog(Cat, Dog):

#     def __init__(self, nickname, weight):
#         super().__init__(nickname, weight)

#     def info(self):
#         return f"{self.nickname}-{self.weight}"


# class DogCat(Dog, Cat):

#     def __init__(self, nickname, weight):
#         super().__init__(nickname, weight)

#     def info(self):
#         return f"{self.nickname}-{self.weight}"


# catDog = CatDog("Sherlock", 24)
# dogCat = DogCat("Simon", 10)

# print(catDog.say())
# print(dogCat.say())


# from collections import UserDict, UserList


# class LookUpKeyDict(UserDict):
#     def lookup_key(self, value):
#         return [key for key in self if self[key] == value]


# print(LookUpKeyDict.lookup_key({"data": 10, "number": 10}, 11))


# class AmountPaymentList(UserList):
#     SUM = 0

#     def amount_payment(self):
#         return sum((x for x in self if x > 0), AmountPaymentList.SUM)


# payments = AmountPaymentList([1, -3, 4])
# print(payments.amount_payment())


# from collections import UserString
# import re


# class NumberString(UserString):
#     def number_count(self):
#         return len(re.sub(r"\D", "", self.data))


# str = NumberString("ewybgx34")
# print(str.number_count())


# class IDException(Exception):
#     pass


# def add_id(id_list, employee_id):

#     if employee_id in id_list:
#         raise IDException(f"Employee ID '{employee_id}' already exists.")

#     if employee_id.startswith("01"):
#         id_list.append(employee_id)
#     else:
#         raise IDException(f"Employee ID '{employee_id}' do not match the requirements.")

#     return id_list


# print(add_id([], "0143535", "024564"))


class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):

        contact = locals().copy()
        del contact["self"]

        contact_with_id = {"id": Contacts.current_id}
        contact_with_id.update(contact)

        self.contacts.append(contact_with_id)
        Contacts.current_id += 1

    def get_contact_by_id(self, id):
        for contact in self.contacts:
            if contact["id"] == id:
                return contact
        return None

    def remove_contacts(self, id):
        for contact in self.contacts:
            if contact["id"] == id:
                self.contacts.remove(contact)
        return None


book = Contacts()
book.add_contacts(
    name="Alice", phone="123456", email="alice@example.com", favorite=True
)
book.add_contacts("Bob", "789012", "bob@example.com", False)

print(book.list_contacts())
print(book.get_contact_by_id(1))
print(book.remove_contacts(1))
print(book.list_contacts())
