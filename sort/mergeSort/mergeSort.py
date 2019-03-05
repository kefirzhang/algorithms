unSortedData = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5, 0]

def mergeSort(data):
    # 基准条件
    if(len(data) <= 1):
        return data
    #递归条件 拆分成两个数组


    size = len(data)//2
    left = mergeSort(data[size:])
    right = mergeSort(data[:size])

    sortedData = []
    while( (len(left) > 0) and (len(right)>0)):
        if(left[0] <= right[0]):
            sortedData.append(left[0])
            del left[0]
        else:
            sortedData.append(right[0])
            del right[0]
    if(len(left) > 0):
        sortedData += left
    if(len(right) > 0):
        sortedData += right

    return sortedData


sortedData = mergeSort(unSortedData)
print(sortedData)
