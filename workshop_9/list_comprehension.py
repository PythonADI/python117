import random

nums = [
    x ** 2
    for x in range(100)
    if x % 2 == 1
]

people = [
    {
        "first_name": f"Name {i}",
        "age": random.randint(18, 45)
    }
    for i in range(100)
]

# nums = []
# for x in range(100):
#     if x % 2 == 1:
#         nums.append(x)

# print(nums)

s = 0
for person in people:
    s += person["age"]

print(people)
print(s / len(people))
