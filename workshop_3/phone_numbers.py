phone_numbers = [
    '+995 555 11 22 33',
    '+995 599 44 55 66',
    '+995 599 77 88 99',
    '+1 555 11 22 33',
    '+1 555 44 55 66',
    '+1 555 77 88 99',
    '+995 599 11 22 33',
    '+995 599 13 76 22',
    '+995 599 99 99 99',
    '+995 595 00 00 00',
    '+995 596 00 00 00',
]

# only send message to Georgian phone numbers
# Georgian phone numbers start with '+995'
print('Hello'.startswith('He'))
for phone_number in phone_numbers:
    if phone_number.startswith('+995') and '599' in phone_number:
        print(f'Send message to {phone_number}')
