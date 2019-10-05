class Solution:
    def findOcurrences(self, text: str, first: str, second: str):
        helper = []
        helper_text = text.split(" ")
        length = len(helper_text)
        i = 0
        while i < length - 2:
            print(helper_text, length, i, helper_text[i])
            if helper_text[i] == first and helper_text[i + 1] == second:
                helper.append(helper_text[i + 2])
            i += 1

        return helper


slu = Solution()
print(slu.findOcurrences("alice is a good girl she is a good student", "a", "good"))
