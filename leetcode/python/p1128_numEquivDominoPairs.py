class Solution:
    def numEquivDominoPairs(self, dominoes) -> int:
        helper = {}
        for i in dominoes:
            i.sort()
            key = tuple(i)
            if helper.__contains__(key):
                helper[key] += 1
            else:
                helper[key] = 1
        ans = 0
        for i in helper:
            if helper[i] > 1:
                ans += (helper[i] * (helper[i] -1 ))/2
        return int(ans)


    def numEquivDominoPairs2(self, dominoes) -> int:
        ans = 0
        for i in range(len(dominoes)):
            for j in range(i + 1, len(dominoes)):
                if dominoes[i][0] == dominoes[j][0] and dominoes[i][1] == dominoes[j][1]:
                    ans += 1
                    continue
                if dominoes[i][0] == dominoes[j][1] and dominoes[i][1] == dominoes[j][0]:
                    ans += 1
                    continue

        return ans


slu = Solution()
print(slu.numEquivDominoPairs([[1, 2], [2, 1], [3, 4], [5, 6]]))
