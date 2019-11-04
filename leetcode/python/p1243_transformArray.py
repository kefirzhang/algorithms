class Solution:
    def transformArray(self, arr):
        while True:
            new_arr = []
            new_arr.append(arr[0])
            for i in range(1, len(arr) - 1):
                if arr[i - 1] < arr[i] and arr[i] > arr[i + 1]:
                    new_arr.append(arr[i] - 1)
                elif arr[i - 1] > arr[i] and arr[i] < arr[i + 1]:
                    new_arr.append(arr[i] + 1)
                else:
                    new_arr.append(arr[i])
            new_arr.append(arr[-1])
            if new_arr == arr:
                break
            else:
                arr = new_arr
        return new_arr


slu = Solution()
print(slu.transformArray([1, 6, 3, 4, 3, 5]))
