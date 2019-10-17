class Solution:
    def maxDistToClosest(self, seats) -> int:
        max_length = 0
        max_start = -1
        max_end = -1
        cur_length = 0
        cur_start = -1
        cur_end = -1

        for i, n in enumerate(seats):

            if n == 0:
                if cur_start == -1:
                    cur_start = i
                cur_length += 1
            else:
                if cur_end == -1:
                    cur_end = i

                # 如果 是左边开头的



                if cur_length > max_length:
                    max_length = max(max_length, cur_length)
                    max_index = i
                cur_length = 0

        print(max_index, max_length)
        return max_length


slu = Solution()
print(slu.maxDistToClosest([0, 0, 0, 0, 0, 0, 1]))
