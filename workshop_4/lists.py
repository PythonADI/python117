nums = [25, 67, 88, 89, 100, -100]

# print(nums[0])

# for i in range(4):
#     print(nums[i])


# for num in nums:
#     print(num / 2)


# Update element in list
# nums[0] = 23
# nums[3] = -7

print(f'Original: {nums}')
for i, num in enumerate(nums):
    nums[i] = abs(num)
    # if num < 0:
    #     nums[i] *= -1
    # num += 1
    # print(num)
print(f'Modified: {nums}')

# nums[0] += 7

nums.append(7)
nums.append(88)
nums.insert(0, 56)
print(nums)
print(f'Middle index: {len(nums) // 2}')
nums.insert(len(nums) // 2, 25)
print(nums)

print('Removing Elements')
print(nums)
for _ in range(5):
    nums.pop()

# nums.remove(-99)
nums.pop(0)
print(nums)
nums.clear()
print(nums)
