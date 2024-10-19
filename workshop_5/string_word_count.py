

'''
You are given a list of strings.
Write a Python program that counts the number of words in each string.
A word is defined as any sequence of characters separated by spaces.
Print each string along with the count of its words.
Use a for loop to iterate through the list of strings and split each string to count the words.
Ignore empty strings in the list.
'''

s = "Print each string along with the count of its words."
space_count = 0

"""
word = ""
while True:
    if character is " ":
        if word is empty:
            dont count this to word
        else:
            end of the word increment word count
    else:
        append character to the word
        not end of word
"""
# for c in s:
#     # print(c)
#     if c == ' ':
#         space_count += 1

# space_count += 1
# print(space_count)
strings = [
    "Print      each string along with the count of its words.",
    "Use a for loop to iterate    through the list of strings and split each string to count the words.",
    "Ignore empty strings in the list.",
    "",
]
# for s in strings:
#     words = []
#     word = ''
#     word_count = 0
#     for i, c in enumerate(s):
#         if i == len(s) - 1 and word != '':
#             # last word case
#             # print(word)
#             word_count += 1
#             # words.append(word)
#             break

#         if c == ' ':
#             if word == '':
#                 continue
#             word_count += 1
#             # print(word)
#             # words.append(word)
#             word = ''
#         else:
#             word += c
#     print(words)
#     print(f'"{s}" has count of {word_count}')


for s in strings:
    words = s.split()
    word_count = len(words)
    print(f'{s} has length: {word_count}')
