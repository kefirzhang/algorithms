class Solution:
    def countCharacters(self, words, chars):
        def isValid(word1, chars1):
            if len(word1) > len(chars1):
                return False
            for i in word1:
                if i in chars1:
                    chars1.remove(i)
                else:
                    return False

            return True

        length = 0
        for word in words:
            if isValid(word, list(chars)):
                length += len(word)

        return length


slu = Solution()
print(slu.countCharacters(["cat", "bt", "hat", "tree"], "atach"))
