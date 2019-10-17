class Solution:
    def duplicateZeros(self, arr) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i, j = 0, len(arr)
        while i < j:
            if arr[i] == 0:
                arr = arr[0:i + 1] + [0] + arr[i + 1:-1]
                i += 2
            else:
                i += 1
        return arr

slu = Solution()
print(slu.duplicateZeros([1,0,2,3,0,4,5,0]))
