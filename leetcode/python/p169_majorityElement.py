class Solution:
    def majorityElement(self, nums):
        map = {}
        if len(nums) == 1:
            return nums[0]
        length = int(len(nums) / 2) + 1
        for i in nums:
            if map.__contains__(i):
                map[i] += 1
                if map[i] == length:
                    return i
            else:
                map[i] = 1
        return

slu = Solution()
print(slu.majorityElement([1,2]))
