import csv
file_path = "./workshop_10/data/data.csv"


with open(file_path) as f:
    data = csv.reader(f)
    friends = []
    for line in data:
        name, age = line
        friends.append({
            "name": name,
            "age": int(age)
        })
        # print(name, age, type(name), type(age))
    
    s = 0
    for friend in friends:
        s += friend["age"]
    print(s / len(friends))
