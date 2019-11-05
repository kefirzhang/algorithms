class Solution:
    def minMoves(self, nums) -> int:
        nums.sort()
        i, j = 0, len(nums) - 1
        ans = 0
        while i < j:
            distance = nums[j] - nums[i]
            ans += distance
            j -= 1
        return ans

    def minMoves2(self, nums) -> int:
        ans = 0
        while True:
            min_index = 0
            max_index = 0
            for index in range(len(nums)):
                if nums[min_index] > nums[index]:
                    min_index = index
                if nums[max_index] < nums[index]:
                    max_index = index

            if min_index == max_index:
                break

            distance = nums[max_index] - nums[min_index]
            for index in range(len(nums)):
                if index != max_index:
                    nums[index] += distance
            ans += distance
        return ans


slu = Solution()
print(slu.minMoves([1, 2, 3]))
