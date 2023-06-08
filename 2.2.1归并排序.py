nums = [1, 3, 5, 9, 0, 4, 5, 7, 2, 8, 6]


def merge_sort(num):
    if len(num) <= 1:  # 地柜便捷条件
        return num  # 到达边界时返回当前的子数组
    mid = int(len(num) / 2)  # 求出数组的中位数
    llist, rlist = merge_sort(num[:mid]), merge_sort(num[mid:])
    result = []
    i, j = 0, 0
    while i < len(llist) and j < len(rlist):
        if rlist[j] < llist[i]:
            result.append(rlist[j])
            j += 1
        else:
            result.append(llist[i])
            i += 1
    result += llist[i:] + rlist[j:]
    return result


print(merge_sort(nums))
