from functools import cmp_to_key
class Solution:
    def reconstructQueue(self, people):
        def cmp(x, y):
            if x[0] > y[0] or (x[0] == y[0] and x[1] < y[1]):
                return 1
            elif x[0] == y[0] and x[1] == y[1]:
                return 0
            else:
                return -1

        people = sorted(people, key=cmp_to_key(lambda x, y: cmp(x, y)), reverse=True)
        res = []
        for i in people:
            res.insert(i[1], i)
        return res
# people.sort(key = lambda x: [-x[0], x[1]])

slu = Solution()
print(slu.reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 2], [5, 0], [6, 1]]))
