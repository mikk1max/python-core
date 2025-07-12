import pickle


class Robot:
    def __init__(self, name, battery_life):
        self.name = name
        self.battery_life = battery_life
        # Цей атрибут ми не збираємось серіалізувати
        self.is_active = False

    def __getstate__(self):
        state = self.__dict__
        # Видаляємо is_active з серіалізованого стану
        del state["is_active"]
        return state

    def __setstate__(self, state):
        # Відновлюємо об'єкт при десеріалізації
        self.__dict__.update(state)
        # Задаємо значення is_active за замовчуванням
        self.is_active = False


robot = Robot("Robo1", 100)

# Серіалізація об'єкта
serialized_robot = pickle.dumps(robot)

# Десеріалізація об'єкта
deserialized_robot = pickle.loads(serialized_robot)

print(deserialized_robot.__dict__)


print("--------------------------------")


import pickle


class Reader:
    def __init__(self, filename):
        self.filename = filename
        self.fh = open(self.filename, "r", encoding="utf-8")

    def close(self):
        self.fh.close()

    def read(self):
        data = self.fh.read()
        return data

    def __getstate__(self):
        attributes = {**self.__dict__, "fh": None}
        return attributes

    def __setstate__(self, state):
        # Відновлюємо стан об'єкта
        self.__dict__ = state
        self.fh = open(state["filename"], "r", encoding="utf-8")


if __name__ == "__main__":
    reader = Reader("./serialization/data.txt")
    data = reader.read()
    print(data)
    reader.close()

    # Приклад серіалізації об'єкта Reader
    with open("./serialization/reader.pkl", "wb") as f:
        pickle.dump(reader, f)

    # Приклад десеріалізації об'єкта Reader
    with open("./serialization/reader.pkl", "rb") as f:
        loaded_reader = pickle.load(f)
        print(loaded_reader.read())
        loaded_reader.close()
