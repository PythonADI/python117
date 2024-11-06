"""
ფაილს თუ ხსნით წაკითხვის რეჟმში რომელიც არ არსებობს
ფაილს თუ ხსნით წაკითხვის რეჟმში რომელიც არსებობს
- all good

ფაილს თუ ხსნით ჩაწერის რეჟმში რომელიც არ არსებობს
- იქმნება ახალი ფაილი ამ დასახელებით

ფაილს თუ ხსნით ჩაწერის რეჟმში რომელიც არსებობს
- წაშლის შიგნით რაც არის (გადააწერს ახალ კონტენტს)

ფაილს თუ ხსნით ჩამატების რეჟმში რომელიც არ არსებობს

"""

import sys


# f = open("./workshop_10/data/numbers.txt")

# print(f.read())
# f.close()

with open("./workshop_10/data/numbers.txt") as f:
    # print(f.read())
    # f.write("Hello")
    s = 0
    length = 0
    # nums = [
    #     int(line.strip())
    #     for line in f.readlines()
    # ]
    f.seek(0)
    for line in f.readlines():
        num = int(line.strip())
        print(type(num), num)
        s += num
        length += 1
    print(s / length, sys.getsizeof(s), sys.getsizeof(length))
    # print(sys.getsizeof(nums))
