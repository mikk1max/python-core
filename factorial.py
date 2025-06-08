def factorial_1(n):
    if n == 0:
        return 1
    else:
        return n * factorial_1(n-1)

def factorial_2(n):
    print("Виклик функції factorial з n = ", n)
    if n == 1:
        print("Базовий випадок, n = 1, повернення 1")
        return 1
    else:
        result = n * factorial_2(n-1)
        print("Повернення результату для n = ", n, ": ", result)
        return result

value = 5
print(f"{value}! = {factorial_2(value)}")
