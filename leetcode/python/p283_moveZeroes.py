class Solution:
    def moveZeroes(self, nums) -> None:
        i, j = 0, 0
        len_nums = len(nums)
        while i < len_nums and j < len_nums:
            print(i, j)
            if nums[i] == 0 and i != len_nums - 1:
                if j < i:
                    j = i + 1
                while j < len_nums - 1 and nums[j] == 0:
                    j += 1
                if nums[j] != 0:
                    nums[i] = nums[j]
                    nums[j] = 0
                    j += 1
            i += 1

        # print(nums)
        """
        Do not return anything, modify nums in-place instead.
        """


slu = Solution()
print(slu.moveZeroes([0, 0]))
