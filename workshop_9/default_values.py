def greet(user = "Roma Annonymous"):
    return f"Hello {user}"


# def expand(lst = None, element = None):
#     if lst is None:
#         lst = []
#     lst.append(element)
#     print(lst)
print(greet())
print(greet("Jigo"))
users = ["test", "test2", "test3"]
# expand(users, "niko")
# print(users)
# expand()
# expand()


def f(x, y = 1, z = 1):
    return (x, y, z)

print(f(3))
print(f(3, 3, 5))
print(f(3, 7))
# keyword agruments
print(f(z=7, y=8, x=10))
print(f(10, y=9, z=10))
print(f(10, z=9, y=10))


