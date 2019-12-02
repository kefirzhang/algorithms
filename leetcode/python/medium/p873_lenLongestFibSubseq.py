class Solution:
    def lenLongestFibSubseq(self, A) -> int:
        dict_set = set(A)
        fib_list = list()
        fib_map = {}
        max_length = 0
        for i in range(len(A)):
            for j in range(i):
                if A[i] - A[j] in dict_set and A[i] - A[j] < A[j]:
                    fib_list.append((A[i], A[j]))

        for i in fib_list:
            if (i[1], i[0] - i[1]) in fib_list:
                fib_map[(i[0], i[1])] = fib_map[(i[1], i[0] - i[1])] + 1
            else:
                fib_map[(i[0], i[1])] = 1
            max_length = max(max_length, fib_map[(i[0], i[1])])
        # print(fib_map)
        return max_length if max_length == 0 else max_length + 2

    def lenLongestFibSubseq2(self, A) -> int:  # 这种是对的 但是时间复杂度比较高 会超时 竟然通过了 set
        length = len(A)
        if length <= 2:
            return 0
        max_length = 0
        helper = set(A)
        for i in range(length):
            for j in range(i + 1, length):
                cur_length = 0
                n, m = A[i], A[j]
                while m + n in helper:
                    cur_length += 1
                    tmp = m
                    m = m + n
                    n = tmp
                max_length = max(max_length, cur_length)
        if max_length == 0:
            return 0
        else:
            return max_length + 2


slu = Solution()
print(slu.lenLongestFibSubseq([2, 4, 7, 8, 9, 10, 14, 15, 18, 23, 32, 50]))
