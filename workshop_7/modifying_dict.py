import pprint
person = {
    "first_name": "Josh",
    "last_name": "Doe",
    "age": 45,
}

print(person)
person["age"] += 1
print(person)
person["pet"] = "doggo"

print(person)

print(person.pop("pet"))
print(person)
print(person.get("first_name"))
# print(person["full_name"])
print(person.get("full_name", "Uknown"))
person.update({
    "age": 27,
    "full_name": "Josh Doe",
    "firends": ["Nick", "Marry", "Joshua"],
})
pprint.pprint(person)
