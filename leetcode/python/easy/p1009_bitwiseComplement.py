class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0:
            return 1
        ret = []
        while N > 0:
            print(N & 1)
            ret.insert(0, "0" if N & 1 == 1 else "1")
            N = N >> 1
        return int("".join(ret), base=2)


slu = Solution()
print(slu.bitwiseComplement(10))
