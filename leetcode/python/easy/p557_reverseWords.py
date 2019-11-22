class Solution:
    def reverseWords(self, s: str) -> str:
        helper = s.split(" ")
        for i, n in enumerate(helper):
            helper[i] = n[::-1]
        return " ".join(helper)


slu = Solution()
print(slu.reverseWords("Let's take LeetCode contest"))
