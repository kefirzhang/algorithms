class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        sort_index = 0
        nlen = len(nums)
        is_transfer = False
        for i in range(nlen - 2, -1, -1):
            if is_transfer:
                break
            for j in range(nlen - 1, i, -1):
                if nums[i] < nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                    sort_index = i + 1
                    is_transfer = True
                    break

        # print(nums, sort_index)
        for i in range(sort_index, nlen):
            for j in range(i + 1, nlen):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]

        print(nums)


slu = Solution()
slu.nextPermutation([1, 3, 2])
'''
[4,2,2,0,0,2,3]
[4,2,0,3,0,2,2]
'''
