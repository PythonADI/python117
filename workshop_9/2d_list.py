import random

WIDTH = 4
HEGHT = 4
treasure_map = [
    [
        random.randint(0, 1)
        for _ in range(WIDTH)
    ]
    for _ in range(HEGHT)
]

treasure_map[random.randint(0, HEGHT - 1)][random.randint(0, WIDTH - 1)] = 2

for row in treasure_map:
    for cell in row:
        print(cell, end="")
    print()

for y, row in enumerate(treasure_map):
    for x, cell in enumerate(row):
        if cell == 2:
            print(f"Found treasure at {x + 1}, {y + 1}")

