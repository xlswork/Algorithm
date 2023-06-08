nums = [1, 3, 5, 9, 0, 4, 5, 7, 2, 8, 6]

for i in range(len(nums) - 1):
    minIndex = i
    for j in range(i, len(nums)):
        if nums[j] < nums[minIndex]:
            minIndex = j
    nums[i], nums[minIndex] = nums[minIndex], nums[i]
print(nums)
