class Geometry:
    PI = 3.14159

    @staticmethod
    def area_of_circle(radius):
        return Geometry.PI * radius**2


print(Geometry.area_of_circle(5))  # 78.53975

print("----------------------------------------------")


class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    @classmethod
    def from_string(cls, employee_info):
        name, position = employee_info.split(",")
        return cls(name, position)


employee_info = "John Doe,Manager"
john_doe = Employee.from_string(employee_info)

print(john_doe.name)  # Виведе: John Doe
print(john_doe.position)  # Виведе: Manager
