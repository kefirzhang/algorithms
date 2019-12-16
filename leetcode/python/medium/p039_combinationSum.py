class Solution:
    def combinationSum(self, candidates, target: int):
        res = []
        for i in candidates:
            if i == target:
                res.append([i])
                continue
            if i > target:
                continue
            ext = self.combinationSum(candidates, target - i)
            for j in ext:
                k = [i] + j
                k.sort()
                if k not in res:
                    res.append(k)
        return res


slu = Solution()
print(slu.combinationSum([2,3,5], 8))
