class Solution:
    def reachNumber(self, target: int) -> int:
        ans = 0
        pos = set()
        pos.add(0)
        while True:
            ans += 1
            if (target - ans) in pos or (target + ans) in pos:
                return ans
            new_pos = set()
            for i in pos:
                new_pos.add(i + ans)
                new_pos.add(i - ans)
            pos = new_pos

        return ans


slu = Solution()
print(slu.reachNumber(2))
