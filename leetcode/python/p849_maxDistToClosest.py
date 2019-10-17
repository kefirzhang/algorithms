class Solution:
    def maxDistToClosest(self, seats) -> int:
        i, j = 0, len(seats) - 1
        left, right = 0, 0
        while i < len(seats) and seats[i] == 0:
            i += 1
            left += 1
        while j >= 0 and seats[j] == 0:
            j -= 1
            right += 1
        middle = 0
        cur_middle = 0
        for i in seats:
            if i == 0:
                cur_middle += 1
            else:
                middle = max(middle, cur_middle)
                cur_middle = 0
        middle = max(middle, cur_middle)

        return max(left, right, int((middle + 1) / 2))


slu = Solution()
print(slu.maxDistToClosest([1, 0, 1, 1, 0,0,0,0, 0, 1]))
