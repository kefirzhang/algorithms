unSortedData = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5, 0]
def quickSort(data):
    # 基准条件
    if (len(data) <= 1):
        return data
    # 递归条件
    pickKey = 0  # 这个key 可以有优化的地方
    pickValue = data[pickKey]
    # 把这个数组拆分成 三部分
    smallerData = []
    biggerData = []
    for index in range(len(data)):
        if (index != pickKey):
            if (data[index] <= pickValue):
                smallerData.append(data[index])
            else:
                biggerData.append(data[index])

    # 递归内容
    return quickSort(smallerData) + [pickValue] + quickSort(biggerData)

sortedData = quickSort(unSortedData)
print(sortedData)
