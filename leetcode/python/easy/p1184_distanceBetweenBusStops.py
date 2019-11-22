class Solution:
    def distanceBetweenBusStops(self, distance, start: int, destination: int) -> int:
        total = sum(distance)
        helper = 0
        if start > destination:
            start, destination = destination, start
        for i in range(start, destination):
            helper += distance[i]
        return min(helper, total - helper)


slu = Solution()
print(slu.distanceBetweenBusStops([7, 10, 1, 12, 11, 14, 5, 0], 7, 2))

'''
[7,10,1,12,11,14,5,0]
7
2
'''
