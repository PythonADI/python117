with open("./numbers____1.txt", "r+") as f:
    f.write("25")
    f.seek(0)
    print(f.read())
