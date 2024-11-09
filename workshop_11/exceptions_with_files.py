
try:
    f = open("./workshop_11/test.txt", "w")
    f.write(str(25 / 7))
except Exception as e:
    print(e)
    print("Something happened")
else:
    print("Hello")
finally:
    print("I will be executed anyway")
    f.close()