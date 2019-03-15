import math

def shellSort(arr):
    n = len(arr)
    gap = math.floor(n/2)
    while gap > 0 :
        for i in range(gap,n):
            cur_step = 0 - gap
            for j in range(i,0,cur_step):
                if arr[j] < arr[j-gap] :
                    tmp = arr[j-gap]
                    arr[j-gap] = arr[j]
                    arr[j] = tmp
                else :
                    break # no more words
        gap = math.floor(gap/2)
    return arr
arr = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5]
print(shellSort(arr))