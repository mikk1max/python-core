def my_generator():
    yield 1
    yield 2
    yield 3


gen = my_generator()

print(next(gen))  # Виведе 1
print(next(gen))  # Виведе 2
print(next(gen))  # Виведе 3

print("-------------------------")


def count_down(start):
    while start > 0:
        yield start
        start -= 1


for number in count_down(5):
    print(number)

print("-------------------------")


def read_lines(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            yield line.strip()


for line in read_lines("jokes\jokes.txt"):
    print(line)
