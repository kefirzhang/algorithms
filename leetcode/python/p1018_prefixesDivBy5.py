class Solution:
    def prefixesDivBy5(self, A):
        num = 0
        ret = []
        for i in A:

            num = 2 * num + i
            if num % 5 == 0:

                ret.append(True)
            else:
                ret.append(False)
        return ret


slu = Solution()
print(slu.prefixesDivBy5([1, 1, 0, 0, 0, 1, 0, 0, 1]))

'''

1, 1, 0, 0, 0, 1, 0, 0, 1
1  2  4  8  16 32 64 128 256
32 + 2 + 1 35 
'''
