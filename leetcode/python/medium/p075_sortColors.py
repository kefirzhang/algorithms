class Solution:
    def sortColors1(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()

    def sortColors2(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero, one, two = 0, 0, 0
        for i in nums:
            if i == 0:
                zero += 1
            elif i == 1:
                one += 1
            else:
                two += 1
        for i in range(0, zero):
            nums[i] = 0
        for i in range(zero, zero + one):
            nums[i] = 1
        for i in range(zero + one, zero + one + two):
            nums[i] = 2

    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0, curr, p2 = 0, 0, len(nums) - 1
        while curr <= p2:
            if nums[curr] == 0:
                nums[p0], nums[curr] = nums[curr], nums[p0]
                curr += 1
                p0 += 1
            elif nums[curr] == 1:
                curr += 1
            else:
                nums[p2], nums[curr] = nums[curr], nums[p2]
                p2 -= 1


slu = Solution()
nums = [2, 0, 2, 1, 1, 0]
slu.sortColors(nums)
print(nums)
