
b = 30
a = 5

def f():
    global a
    a += 7
    print("Local a:", a)

def increment(a):
    return a + 7
f()
f()

print("Global a:", a)
a = increment(a)
b = increment(b)
a = increment(a)
a = increment(a)
print("Global a:", a)
print("Global b:", b)

