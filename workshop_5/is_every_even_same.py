import random

for _ in range(10):
    n = random.randint(100_000, 1_000_000)

    n_str = str(n)
    first_num = n_str[0]
    is_good = True
    for num in n_str[::2]:
        if first_num != num:
            is_good = False
            break

    if is_good:
        print(n, 'გვაწყობს!')
    else:
        print(n, 'არ გვაწყობს!')