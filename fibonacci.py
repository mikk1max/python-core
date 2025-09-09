def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

value = 11
print(f"FIB({value}) = {fibonacci(value)}")

def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b

print(f"fibonacci_iterative(10) = {fibonacci_iterative(10)}")
