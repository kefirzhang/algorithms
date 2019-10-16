class Solution:
    def checkPossibility(self, nums) -> bool:
        i, length, change_times = 0, len(nums), 0

        while i < length - 1:
            if nums[i] > nums[i + 1]:
                change_times += 1
                if i != 0:
                    if nums[i+1] < nums[i-1]:
                        nums[i + 1] = nums[i]
            if change_times > 1:
                return False
            i += 1
        if change_times > 1:
            return False
        return True


slu = Solution()
print(slu.checkPossibility([ 4, 2, 3]))
