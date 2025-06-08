str = input("Enter a string >>> ")

def calculate(str):
    total_chars = len(str)
    space_count = 0

    for char in str:
        if char == " ":
            space_count += 1

    print(f"Total chars = {total_chars}")
    print(f"Quantity of spaces = {space_count}")

calculate(str)