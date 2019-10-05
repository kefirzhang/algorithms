class Solution:
    def shortestCompletingWord(self, licensePlate, words):
        helper_plate = []
        for i in licensePlate:
            if ord('a') <= ord(i) <= ord('z') or ord('A') <= ord(i) <= ord('Z'):
                helper_plate.append(i.lower())

        min_word = False
        for word in words:
            tmp_word = list(word)
            word_match = True
            for i in helper_plate:
                if i in tmp_word:
                    tmp_word.remove(i)
                else:
                    word_match = False

            if word_match is True:
                if min_word is False:
                    min_word = word
                elif len(word) < len(min_word):
                    min_word = word

        return min_word


slu = Solution()
print(slu.shortestCompletingWord("1s3 456", ["bbbbbbbb", "looks", "pest", "stew", "show", 'ab']))
