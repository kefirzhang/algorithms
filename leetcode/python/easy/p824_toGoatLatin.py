class Solution:
    def toGoatLatin(self, S: str) -> str:
        words = S.split(" ")
        helper = []
        for i, word in enumerate(words):
            if word[0] in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
                word = word + "ma" + "a" * (i + 1)
            else:
                word = word[1:] + word[0] + "ma" + "a" * (i + 1)
            helper.append(word)
        return " ".join(helper)


slu = Solution()
print(slu.toGoatLatin("Each word consists of lowercase and uppercase letters only"))
