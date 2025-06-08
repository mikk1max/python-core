x = int(input("Enter the x value >>> "))
y = int(input("Enter the y value >>> "))

if x >= 0:
    if y >= 0:  # x > 0, y > 0
        print("First quadrant")
    else:  # x > 0, y < 0
        print("Fourth quadrant")
else:
    if y >= 0:  # x < 0, y > 0
        print("Second quadrant")
    else:  # x < 0, y < 0
        print("Third quadrant")



point = (1, 0)

match point:
    case (0, 0):
        print("Точка в центрі координат")  
    case (0, y):
        print(f"Точка лежить на осі Y: y={y}")  
    case (x, 0):
        print(f"Точка лежить на осі X: x={x}") 
    case (x, y):
        print(f"Точка має координати:  x={x}, y={y}") 
    case _:
        print("Це не точка")
