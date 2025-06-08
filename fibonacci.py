def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

value = 11
print(f"FIB({value}) = {fibonacci(value)}")
