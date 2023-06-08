nums = [1, 3, 5, 9, 0, 4, 5, 7, 2, 8, 6]

for i in range(len(nums), 0, -1):
    flag = 0
    for j in range(i - 1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
            flag = 1
    if not flag:
        break

print(nums)
