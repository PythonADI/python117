names = ["Gio", "Jorje", "James"]
ages = [15, 23, 24]

# names.pop()
# names.pop()
# names.pop()
# names.pop()

for i in range(len(names)):
    print(f'Iteration {i}')
    names.pop()
    ages.pop()

print(names)