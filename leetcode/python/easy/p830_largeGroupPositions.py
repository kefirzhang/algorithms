class Solution:
    def largeGroupPositions(self, S: str):
        start = 0
        i = 0
        helper = []

        while i < len(S) - 1:
            print(i, S[i], start, i - start)
            if S[i] != S[i + 1]:
                if i - start >= 2:
                    helper.append([start, i])
                start = i + 1

            i += 1
        if i - start >= 2:
            helper.append([start, i])

        return helper


slu = Solution()
print(slu.largeGroupPositions("abbxxxxzzyyyy"))
