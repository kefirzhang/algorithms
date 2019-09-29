class Solution:
    def peakIndexInMountainArray(self, A):
        length = len(A)
        left = 0
        right = length - 1
        mid = int((right - left + 1) / 2)
        while not (A[mid - 1] < A[mid] and A[mid] > A[mid + 1]):
            print(mid, A[mid])
            if A[mid] > A[mid - 1]:
                left = mid
                mid = mid + int((right - left + 1) / 2)
            else:
                right = mid
                mid = left + int((right - left + 1) / 2)

        return mid


slu = Solution()
print(slu.peakIndexInMountainArray([0, 1, 2, 3, 4, 5, 6, 11, 10, 9, 8, 0]))
