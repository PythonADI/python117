person = {
    "name": "Josh",
    "friends": [
        {
            "name": "Nick",
            "age": 16
        },
        {
            "name": "Gio",
            "age": 33
        },
        {
            "name": "Mary",
            "age": 26
        }
    ]
}

# calculate avg age of friends
s = 0
for friend in person["friends"]:
    s += friend["age"]

print(s / len(person["friends"]))
