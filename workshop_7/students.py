import random
import pprint

students = []

for i in range(3):
    students.append({
        "name": f"Student {i}",
        "subjects": [
            {
                "name": "Math",
                "grade": random.randint(40, 100)
            },
            {
                "name": "Linear Algebra",
                "grade": random.randint(40, 100)
            }
        ]
    })

pprint.pprint(students)
for student in students:
    print(student["name"])
    # print(student["subjects"][0]["grade"])
    s = 0
    for subject in student["subjects"]:
        s += subject["grade"]
        if subject["grade"] >= 51:
            print(f"{subject['name']} Passed ({subject['grade']}/100)")
        else:
            print(f"{subject['name']} Failed ({subject['grade']}/100)")

    print('AVG grade: ', s / len(student["subjects"]))
