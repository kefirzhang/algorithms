class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        helper = {
            'b': 0,
            'a': 0,
            'l': 0,
            'o': 0,
            'n': 0
        }
        for i in text:
            if helper.__contains__(i):
                helper[i] += 1

        helper['l'] = int(helper['l'] / 2)
        helper['o'] = int(helper['o'] / 2)
        num = helper['b']
        for i in helper:
            num = min(num, helper[i])

        return num


slu = Solution()
print(slu.maxNumberOfBalloons("loonbalxballpoon"))
