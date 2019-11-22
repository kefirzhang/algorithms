class Solution:
    def findPairs(self, nums, k: int) -> int:
        nums.sort()
        len_nums = len(nums)
        helper = []
        if len_nums <= 1:
            return 0
        i, j, total_k = 0, 1, 0

        while i < len_nums and j < len_nums:
            if i >= j:
                j += 1
                continue
            distance = nums[j] - nums[i]
            if distance == k:
                if nums[i] not in helper:
                    helper.append(nums[i])
                    total_k += 1
                i += 1
                j += 1
            elif nums[j] - nums[i] < k:
                j += 1
            elif nums[j] - nums[i] > k:
                i += 1

        return total_k


slu = Solution()
print(slu.findPairs([1, 1, 1, 1, 1], 0))
