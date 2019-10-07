class Solution:
    def findWords(self, words):
        keybord = [
            "qwertyuiop",
            "asdfghjkl",
            "zxcvbnm",
        ]
        helper = []
        for word in words:

            for line in keybord:
                is_in_one = True
                for i in word:
                    if i.lower() not in line:
                        is_in_one = False
                if is_in_one is True:
                    helper.append(word)

        return helper


slu = Solution()
print(slu.findWords(["Hello", "Alaska", "Dad", "Peace"]))
