# first_name = input("Enter your first name: ")
# age = int(input("Enter your age: "))
first_name = 'George'
age = 25
is_adult = age >= 18

print(first_name, type(first_name))
print(f'You are an adult {is_adult}')
print(f'You name contains {len(first_name)} characters')
print(f'first character is: {first_name[0]}')
print(f'last character is: {first_name[len(first_name) - 1]}')

