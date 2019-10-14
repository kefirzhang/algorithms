class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and s[i] not in vowel:
                i += 1
            while j > i and s[j] not in vowel:
                j -= 1
            if i < j:
                # print(i, j, s[i], s[j], s)
                tmp = s[i]
                s[i] = s[j]
                s[j] = tmp
                i += 1
                j -= 1

        return "".join(s)


slu = Solution()
print(slu.reverseVowels("leetcode"))
'''
"leotcede"
'''
