class Solution:
    def topKFrequent(self, nums, k: int):
        topk = {}
        for i in nums:
            if topk.__contains__(i):
                topk[i] += 1
            else:
                topk[i] = 1
        helper = []
        for i in topk:
            helper.append(topk[i])
        helper.sort()
        n = helper[-k]
        res = []
        for i in topk:
            if topk[i] >= n:
                res.append(i)
        return res


slu = Solution()
print(slu.topKFrequent([1, 1, 1, 2, 2, 3], 2))
