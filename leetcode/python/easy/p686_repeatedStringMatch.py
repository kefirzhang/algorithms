class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        if B in A:
            return 1
        helper = A
        min_times = int((len(A)*2 + len(B))/len(A))+1
        for i in range(1, min_times):
            helper += A
            if B in helper:
                # print(helper)
                return i + 1

        return -1


slu = Solution()
print(slu.repeatedStringMatch("abcd", "cdabcdab"))
'''
"abcd"
"cdabcdab"
'''