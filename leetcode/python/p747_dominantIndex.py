class Solution:
    def dominantIndex(self, nums) -> int:
        if len(nums) <= 1:
            return 0
        if nums[0] > nums[1]:
            m, n = 0, 1
        else:
            m, n = 1, 0
        i = 0
        # print(m, n)
        while i < len(nums):
            # print(i)
            if nums[i] > nums[m]:
                n = m
                m = i
            elif nums[i] > nums[n] and i != m:
                n = i
            i += 1
        # print(m, n)
        if nums[m] >= 2 * nums[n]:
            return m
        else:
            return -1


slu = Solution()
print(slu.dominantIndex([1, 0]))
