first_name = list("Jhonny")


print(first_name)
print(first_name[:3])
print(first_name[-3:])
print(first_name[::3])
print(first_name[:] is first_name)

# x = first_name.copy()
x = first_name[:]

print(x, first_name)
x.append('.')
print(x, first_name)

# for i in range(0, 10, 2):
#     print(i)
