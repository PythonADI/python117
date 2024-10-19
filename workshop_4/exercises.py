# Count vowels in string

PI = 3.14
FIRST_NAME = 'name'

a = f'test {PI}'
n = [1, 2, 3, 4, 5]

for i, num in enumerate(n):
    print(i, num)


g = a[:]
g[0] = 'F'
print(g is a)
print(g, a)

print(n.copy())
print(n[::], n[:] is n)
print(a[:], a[:] is a)
print(n[::-1])

'''
Write a program that prints all even numbers up to the number given by user
'''


