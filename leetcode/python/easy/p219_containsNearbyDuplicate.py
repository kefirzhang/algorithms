class Solution:
    def containsNearbyDuplicate(self, nums, k) -> bool:
        helper_map = {}
        for i, n in enumerate(nums):
            if helper_map.__contains__(n):
                if i - helper_map[n] <= k:
                    return True
            helper_map[n] = i

        return False


slu = Solution()
print(slu.containsNearbyDuplicate([1, 2, 3, 1], 3))
