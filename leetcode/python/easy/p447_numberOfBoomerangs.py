class Solution:

    def numberOfBoomerangs(self, points) -> int:
        def distance(point1, point2):
            return (point1[0] - point2[0]) * (point1[0] - point2[0]) + (point1[1] - point2[1]) * (point1[1] - point2[1])

        ans = 0
        helper = {}
        for i in range(len(points)):
            for j in range(len(points)):
                if i == j:
                    continue
                cur_distance = distance(points[i], points[j])
                if helper.__contains__(cur_distance):
                    helper[cur_distance] += 1
                else:
                    helper[cur_distance] = 1
            for num in helper.values():
                ans += num * (num - 1)
            helper = {}

        return ans


slu = Solution()
print(slu.numberOfBoomerangs([[0, 0], [1, 0], [2, 0]]))
