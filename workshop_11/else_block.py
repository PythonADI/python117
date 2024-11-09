def get_name():
    name = "hello" # input("Name")

    if not name.isalpha():
        raise ValueError("Please enter correct name format")

    return name


try:
    name = get_name()
except ValueError:
    print('...')
else:
    print(f"Hello {name}")
    try:
        print(name + 27)
    except TypeError:
        print("NO no NO")
