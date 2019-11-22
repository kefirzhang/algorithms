class Solution:
    def shortestToChar(self, S: str, C: str):
        length = len(S)
        ret = []
        for i, n in enumerate(S):
            x, y = i, i
            left_length, right_length = length, length
            while x >= 0:
                if S[x] == C:
                    left_length = i - x
                    break
                x -= 1
            while y < length:
                if S[y] == C:
                    right_length = y - i
                    break
                y += 1
            ret.append(min(left_length, right_length))

        return ret


slu = Solution()
print(slu.shortestToChar("baaa","b"))
