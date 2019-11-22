class Solution:
    def rotatedDigits(self, N: int) -> int:
        # 1-》 2 5 6 9 0 -》 0 1 8  -1 3 4 7
        helper = [0, 0, 1, -1, -1, 1, 1, -1, 0, 1]
        total = 0
        for i in range(1, N + 1):
            i = str(i)
            if len(i) <= 1:
                if helper[int(i)] == 1:
                    total += 1
                    print(i)
            else:
                left = int(i[:-1])
                right = int(i[-1])
                if helper[left] == -1 or helper[right] == -1:
                    helper.append(-1)

                elif helper[left] == 0 and helper[right] == 0:
                    helper.append(0)
                else:
                    helper.append(1)
                    total += 1

                    # print(i)

        return total


slu = Solution()
print(slu.rotatedDigits(100))
