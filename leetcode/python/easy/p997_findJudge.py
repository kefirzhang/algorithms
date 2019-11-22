class Solution:
    def findJudge(self, N: int, trust) -> int:
        helper = [set() for i in range(N)]
        for i, n in enumerate(trust):
            helper[n[0] - 1].add(n[1])

        for i in range(N):
            if len(helper[i]) != 0:
                continue
            is_major = True
            for j, n in enumerate(helper):
                if j == i:
                    continue
                else:
                    if i + 1 not in n:
                        is_major = False
            if is_major:
                return i + 1
        return -1


slu = Solution()
print(slu.findJudge(1, []))
