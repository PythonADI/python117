# age = int(input('Age: '))

# under 10 -> free
# under 20 -> 0.5
# under 50 -> 2
# -> 1

# over 10 -> 0.5
# over 20 -> 2
# over 50 -> 1
# -> free

age = 13

if age < 20:
    print('<10')
elif age < 10:
    print('<20')
else:
    print('ყველა დანარჩენი')
