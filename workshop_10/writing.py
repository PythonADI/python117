with open("./numbers.txt", "w") as f:
    nums = [
        i
        for i in range(10)
    ]
    # nums = list(range(10))
    for i in range(10):
        f.write(f'{i}\n')
    f.write("27\n")
    f.write("27\n")
    # str_nums = []
    # for n in nums:
    #     str_nums.append(str(n))
    f.writelines([
        f'{n}\n' for n in nums
    ])

