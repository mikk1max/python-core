def outer_function(msg):
    message = msg

    def inner_function():
        print(message)

    return inner_function


my_func = outer_function("Hello, world!")
my_func()


print("-------------------------")


from typing import Callable


def counter() -> Callable[[], int]:
    count = 0

    def increment() -> int:
        # використовуємо nonlocal, щоб змінити змінну в замиканні
        nonlocal count
        count += 1
        return count

    return increment


# Створення лічильника
count_calls = counter()

# Виклики лічильника
print(count_calls())  # Виведе 1
print(count_calls())  # Виведе 2
print(count_calls())  # Виведе 3
