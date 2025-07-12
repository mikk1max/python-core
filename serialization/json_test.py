import json

some_data = {
    "key": "value",
    2: [1, 2, 3],
    "my_tuple": (5, 6),
    "my_dict": {"key": "value"},
}

json_string = json.dumps(some_data)
print(json_string)
unpacked_some_data = json.loads(json_string)
print(unpacked_some_data)


print("--------------------------------")

data = {"name": "Gupalo Vasyl", "age": 30, "isStudent": True}

# Серіалізація у файл
with open("./serialization/data.json", "w", encoding="utf-8") as f:
    json.dump(data, f)

# Десеріалізація з файлу
with open("./serialization/data.json", "r", encoding="utf-8") as f:
    data_from_file = json.load(f)
    print(data_from_file)


print("--------------------------------")


data = {"name": "Гупало Василь", "age": 30, "isStudent": True}

# Серіалізація у файл
with open("./serialization/data_new.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
