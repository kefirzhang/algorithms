class Solution:
    def sumEvenAfterQueries(self, A, queries):
        base = 0
        for i in A:
            if i % 2 == 0:
                base += i

        ret = []
        for querie in queries:
            index = querie[1]
            val = querie[0]
            pre = A[index]
            after = A[index] + val
            A[index] = after
            if pre % 2 == 0:
                if after % 2 == 0:
                    base += val
                else:
                    base -= pre
            else:
                if after % 2 != 0:
                    1
                else:
                    base += after
            ret.append(base)

        return ret

    def sumEvenAfterQueries2(self, A, queries):
        ret = []
        for querie in queries:
            A[querie[1]] += querie[0]
            total = 0
            for i in A:
                if i % 2 == 0:
                    total += i
            ret.append(total)

        return ret


slu = Solution()
print(slu.sumEvenAfterQueries([1, 2, 3, 4], [[1, 0], [-3, 1], [-4, 0], [2, 3]]))
