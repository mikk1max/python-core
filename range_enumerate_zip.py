print("[----range----]")
for i in range(0, 14, 2):
    print(i, end=" ")

print("\n[--enumarate--]")

some_list = ["apple", "banana", "cherry"]
for index, value in enumerate(some_list):
    print(index, value)

print("[-----zip-----]")

list1 = ["green", "delicious", "red"]
list2 = ["apple", "cherry", "tomato"]
for number, letter in zip(list1, list2):
    print(number, letter)

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c', 'd', 'e']

for number, letter in zip(list1, list2):
    print(number, letter)
