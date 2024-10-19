'''
Write a Python program that iterates over the numbers from 1000 to 50, 
decrementing by 5 using a loop. For each number, 
print the number if it is a palindrome (reads the same forward and backward). 
Skip non-palindromes using continue.
'''
import math

# for n in range(1000, 50, -5):
#     n_str = str(n)
#     is_palindrome = True
#     for i in range(len(n_str) // 2):
#         lp = i
#         rp = -i - 1

#         if n_str[lp] != n_str[rp]:
#             is_palindrome = False
#             break
#     if is_palindrome:
#         print(f'{n} is palindrome')

for n in range(1000, 50, -5):
    n_str = str(n)
    lmid = len(n_str) // 2
    rmid = math.ceil(len(n_str) / 2)
    is_palindrome = n_str[:lmid] == n_str[rmid:]
    # print(lmid, rmid)
    # print(n_str[:lmid], n_str[rmid:])
    if is_palindrome:
        print(f'{n} is palindrome')


n = 797870