names = ["Joe", "Trump", "Kamala", 'Trump']

# for name in names:
#     if name == 'Trump':
#         continue
#     print(f'Candidate of US persident: {name}')


for name in names:
    if name != 'Trump':
        # Guard Clause
        continue
    print(f'Sending message to: {name}')



