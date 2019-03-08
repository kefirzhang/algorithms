def selectionSort(arr):
    arrLen = len(arr)
    for i in range(1, arrLen):
        maxIndex = 0
        for j in range(0, arrLen - i + 1):
            if (arr[maxIndex] < arr[j]):
                maxIndex = j

        tmpValue = arr[arrLen - i]
        arr[arrLen - i] = arr[maxIndex]
        arr[maxIndex] = tmpValue

    return arr


arr = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5]
print(selectionSort(arr))
