nums = [1, 3, 5, 9, 0, 4, 5, 7, 2, 8, 6]

new_nums = []

while len(nums):
    minIndex = 0
    for i in range(1, len(nums)):
        if nums[i] < nums[minIndex]:
            minIndex = i
    temp = nums[minIndex]
    nums.pop(minIndex)
    new_nums.append(temp)

print(new_nums)