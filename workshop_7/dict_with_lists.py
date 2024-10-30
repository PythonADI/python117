student = {
    "name": "Jenny",
    "subjects": [
        "Math",
        "Georgaphy",
        "Chemistry",
    ],
    "pet": {
        "name": "bobo",
        "age": 6,
        "type": "parrot",
    },
}
print(student["name"], student["subjects"])
# print(student["pet"]["name"])
print(student["pet"]["name"], student["pet"]["type"])
pet = student["pet"]
print(pet["name"], pet["type"])
print(student["subjects"][0], student["subjects"][2])
print(student["subjects"][::2])
