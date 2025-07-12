import pickle

my_data = {"key": "value", "num": 42}

serialized_data = pickle.dumps(my_data)
print(serialized_data)

deserialized_data = pickle.loads(serialized_data)
print(deserialized_data)


print("--------------------------------")


my_data = {"key": "value", "num": 100}

with open("./serialization/data.pickle", "wb") as file:
    pickle.dump(my_data, file)


with open("./serialization/data.pickle", "rb") as file:
    deserialized_data = pickle.load(file)

print(deserialized_data)


print("--------------------------------")


class Human:
    def __init__(self, name):
        self.name = name


bob = Human("Bob")
with open("./serialization/instance.pickle", "wb") as file:
    pickle.dump(bob, file)


with open("./serialization/instance.pickle", "rb") as file:
    loaded_instance = pickle.load(file)

print(loaded_instance.name)


print("--------------------------------")


# Збереження налаштувань
settings = {"theme": "dark", "language": "ukrainian"}
with open("./serialization/settings.pickle", "wb") as f:
    pickle.dump(settings, f)

# Завантаження налаштувань
with open("./serialization/settings.pickle", "rb") as f:
    loaded_settings = pickle.load(f)

print(loaded_settings)
