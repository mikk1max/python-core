my_list = [1, 2, 3]


def square_list(x: list):
    return [el**2 for el in x]


new_list = square_list(my_list)
print(new_list)
print(my_list)


print("--------------------------------")


my_list = [1, 2, 3]
copy_list = my_list[:]
copy_list.append(4)
print(my_list, copy_list)

my_dict = {1: "a"}
copy_dict = {**my_dict}
copy_dict["new_key"] = "new_value"
print(my_dict, copy_dict)


print("--------------------------------")


import copy

my_list = [1, 2, {"name": "Gupalo Vasyl"}]
copy_list = copy.copy(my_list)
copy_list.append(4)
print(my_list)
print(copy_list)


copy_list[2]["age"] = 30
print(my_list)
print(copy_list)


print("--------------------------------")


my_list = [1, 2, {"name": "Gupalo Vasyl"}]
copy_list = copy.deepcopy(my_list)
copy_list[2]["age"] = 30
print(my_list)
print(copy_list)


print("--------------------------------")


class SimpleObject:
    def __init__(self, greeting: str):
        self.greeting = greeting


class ComplexObject:
    def __init__(self, value: int, nested_obj: SimpleObject):
        self.value = value
        self.nested_obj = nested_obj

    def __copy__(self):
        print("Викликано __copy__ для ComplexObject")
        # Поверхневе копіювання не копіює вкладені об'єкти глибоко
        return ComplexObject(self.value, self.nested_obj)

    def __deepcopy__(self, memo=None):
        print("Викликано __deepcopy__ для ComplexObject")
        # Глибоке копіювання копіює вкладені об'єкти
        return ComplexObject(
            copy.deepcopy(self.value, memo), copy.deepcopy(self.nested_obj, memo)
        )


nested_obj = SimpleObject("Привіт")
complex_obj = ComplexObject(5, nested_obj)

# Створюємо копію та глибоку копію
complex_obj_copy = copy.copy(complex_obj)
complex_obj_deepcopy = copy.deepcopy(complex_obj)

# Змінюємо значення вкладеного об'єкту nested_obj
nested_obj.greeting = "Hello"

# Дивимось зміни у об'єктах
print(f"Copy object: {complex_obj_copy.nested_obj.greeting}")
print(f"Deepcopy object: {complex_obj_deepcopy.nested_obj.greeting}")


print("--------------------------------")


class UserSettings:
    def __init__(self, preferences, large_data_reference):
        self.preferences = preferences
        self.large_data_reference = large_data_reference

    def __deepcopy__(self, memo):
        print("Кастомізоване глибоке копіювання для UserSettings")
        # Припустимо, що preferences - це невеликий словник, який можна безпечно скопіювати,
        # а large_data_reference - це посилання на великий об'єкт даних, яке ми не хочемо дублювати.
        new_preferences = copy.deepcopy(self.preferences, memo)
        # Передаємо посилання на ті ж великі дані замість їх копіювання
        new_obj = UserSettings(new_preferences, self.large_data_reference)
        return new_obj


# Створення екземпляра UserSettings
original_settings = UserSettings({"language": "uk"}, large_data_reference="LargeDataID")

# Глибоке копіювання з кастомізованою логікою
settings_copy = copy.deepcopy(original_settings)
