class Solution:
    def subarraySum(self, nums, k: int) -> int:
        hashmap = {}
        hashmap[0] = 1
        sum = 0
        count = 0
        for i in nums:
            sum += i
            if hashmap.__contains__(sum - k):
                count = count + hashmap[sum - k]
            if hashmap.__contains__(sum):
                hashmap[sum] += 1
            else:
                hashmap[sum] = 1
        return count


slu = Solution()
print(slu.subarraySum([0,0,0,0,0,0,0,0,0,0], 0))
