class Solution:
    def threeSum(self, nums):
        ret = []
        helper = set()
        nums.sort()
        n = len(nums)
        if n < 3:
            return []
        for i in range(n):

            if nums[i] > 0:
                return ret
            j = i + 1
            k = n - 1
            while j < k:

                if nums[i] + nums[j] + nums[k] == 0:
                    if tuple([nums[i], nums[j], nums[k]]) not in helper:
                        ret.append([nums[i], nums[j], nums[k]])
                        helper.add(tuple([nums[i], nums[j], nums[k]]))
                    j += 1
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1

        return ret


slu = Solution()
print(slu.threeSum([-2, 0, 1, 1, 2]))
