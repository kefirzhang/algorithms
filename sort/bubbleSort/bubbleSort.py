
def bubbleSort(arr):
    arr_len = len(arr)
    for i in range(1, arr_len):
        for j in range(0,arr_len - i):
            if arr[j] > arr[j+1]:
                tmp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = tmp
    return arr

arr = [10,1,9,2,8,3,7,4,6,5]
print(bubbleSort(arr))