import random

class Person:
    def __init__(self, name, age):
        # constructor / initializer
        self.name = name
        self.age = age
        self.friends = []

    def add_friend(self, other):
        if self is other:
            raise ValueError("You are trying to befriend same person!")
        # setter
        if other in self.friends or self in other.friends:
            raise ValueError(f"{other.name} has already befriended {self.name}")

        self.friends.append(other)
        other.friends.append(self)

    def unfriend(self, other):
        self.friends.remove(other)
        other.friends.remove(self)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
    

# instatiate
# object or instance
# p = Person("Joe")

people = [
    Person(f"Person {i}", i + 10)
    for i in range(10)
]

people[0].name = "Nick"
# Dont this
# people[0].gender = "Dog"

people[-1].name = "Goegre"
# people[0].friends.append(people[0])


# people[0].friends.append(people[-1])
# people[-1].friends.append(people[0])
for _ in range(10):
    # p1 = people[random.randint(0, len(people) - 1)]
    # p2 = people[random.randint(0, len(people) - 1)]
    try:
        random.choice(people).add_friend(random.choice(people))
    except ValueError:
        continue

# people[0].add_friend(people[-1])
# people[0].add_friend(people[-1])
# people[0].add_friend(people[-1])
# people[0].add_friend(people[-1])



print(people[0])
print(people[0].friends)

for p in people:
    print(p.name, p.age)
    for firend in p.friends:
        print(f"{p.name} has friend {firend.name}")
# print(p.name)
# p2 = Person("Jane")
# print(p2.name)
