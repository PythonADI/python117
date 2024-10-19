'''
write a program that prints all prime numbers up to the number given by user
'''
import math

N = 1000

for n in range(2, N):
    is_prime = True
    for x in range(2, int(math.sqrt(n)) + 1):
        if n % x == 0:
            is_prime = False
            break

    if is_prime:
        print(n)
    # print(f'{n} is prime: {is_prime}')
