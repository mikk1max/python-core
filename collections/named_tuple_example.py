import collections

Person = collections.namedtuple(
    "Person", ["first_name", "last_name", "age", "birth_place", "post_index"]
)

person = Person("Mick", "Nitch", 35, "Boston", "01146")

print(person.first_name)
print(person.post_index)
print(person.age)
print(person[3])


Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])

cat = Cat("Simon", 4, "Krabat")

print(f"This is a cat {cat.nickname}, {cat.age} age, his owner {cat.owner}")
