nums = [1, 3, 5, 9, 0, 4, 5, 7, 2, 8, 6]

for i in range(1, len(nums)):
    for j in range(i):
        if nums[j] > nums[i]:
            inc = nums[i]
            nums.pop(i)
            nums.insert(j, inc)
            break

print(nums)
