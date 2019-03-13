def insertionSort(arr):
    n = len(arr)
    for i in range(0, n):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                tmp = arr[j - 1]
                arr[j - 1] = arr[j]
                arr[j] = tmp

    return arr


arr = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5]
print(insertionSort(arr))
