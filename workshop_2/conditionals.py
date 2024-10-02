# is_admin = input('Are you an admin? ') == 'yes'
is_admin = True

if is_admin:
    # code block / fragment
    secret_text = 'Secret Text'
    print(secret_text)
else:
    print('You have no permission!')



age = int(input("How old are you? "))

if age >= 21:
    print('Pay 10$')
else:
    print('Free drinks')
