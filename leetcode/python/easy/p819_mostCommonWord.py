class Solution:
    def mostCommonWord(self, paragraph: str, banned) -> str:
        helper = {}
        tmp_word = ""
        for i in paragraph:
            if (ord('a') <= ord(i) <= ord('z') or ord('A') <= ord(i) <= ord('Z')) is False:
                if len(tmp_word) > 0:
                    if helper.__contains__(tmp_word):
                        helper[tmp_word] += 1
                    else:
                        helper[tmp_word] = 1
                    tmp_word = ""
            else:
                tmp_word += i.lower()
        if len(tmp_word) > 0:
            if helper.__contains__(tmp_word):
                helper[tmp_word] += 1
            else:
                helper[tmp_word] = 1

        max_times = 0
        max_word = ""
        print(helper)
        for word in helper:
            if helper[word] > max_times and word not in banned:
                max_times = helper[word]
                max_word = word
        return max_word


slu = Solution()
print(slu.mostCommonWord("Bob", ["hit"]))

'''
"Bob hit a ball
the hit BALL flew far after it was hit. Bob hit a ball
the hit BALL flew far after it was hit. Bob hit a ball
the hit BALL flew far after it was hit. Bob hit a ball
the hit BALL flew far after it was hit. Bob hit a ball
the hit BALL flew far after it was hit. Bob hit a ball
the hit BALL flew far after it was hit. Bob hit a ball
the hit BALL flew far after it was hit. Bob hit a ball
the hit BALL flew far after it was hit. Bob hit a ball
the hit BALL flew far after it was hit. Bob hit a ball
the hit BALL flew far after it was hit. Bob hit a ball
the hit BALL flew far after it was hit. Bob hit a ball
the hit BALL flew far after it was hit. Bob hit a ball
the hit BALL flew far after it was hit. Bob hit a ball
the hit BALL flew far after it was hit. Bob hit a ball
the hit BALL flew far after it was hit. "
["hit"]

"Bob hit a ball, the hit BALL flew far after it was hit."
["hit"]
'''