users = [
    'Gio',
    'Nick',
    'Jorje',
    'Mary',
    'Nina',
    'Gocha',
]

print('Copy:', users.copy())
print('Original:', users)
print(users.copy() is users)
u2 = users.copy()
u2[0] = 'Nika'
print(u2)
print(users)

# for _ in range(len(users)):
for user in users.copy():
    # print(f'{user} bought the ticket')
    print(f'{users.pop(0)} bought the ticket')


