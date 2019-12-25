class Solution:
    def searchRange(self, nums, target: int):
        nlen = len(nums)
        if nlen == 0:
            return [-1, -1]
        start, end = 0, nlen - 1
        while start <= end:
            mid = int((start + end) / 2)

            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                left, right = mid, mid
                print(mid)
                while left > 0 and nums[left - 1] == target:
                    left -= 1
                while right < nlen - 1 and nums[right + 1] == target:
                    right += 1
                return [left, right]

        return [-1, -1]


slu = Solution()
print(slu.searchRange([2, 2], 2))
