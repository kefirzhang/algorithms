class Solution:
    def containsDuplicate(self, nums) -> bool:
        helper_set = set()
        for i in nums:
            if i in helper_set:
                return True
            else:
                helper_set.add(i)
        return False


slu = Solution()
print(slu.containsDuplicate([1, 2, 3]))
