class Solution:
    def findShortestSubArray(self, nums) -> int:
        helper_map = {}
        for i, n in enumerate(nums):
            if helper_map.__contains__(n):
                helper_map[n]['num'] += 1
                helper_map[n]['end'] = i
            else:
                helper_map[n] = {'num': 1, 'start': i, 'end': i}
        max_step = {'num': 0, 'start': 0, 'end': 0}
        for n in helper_map.values():
            if n['num'] > max_step['num']:
                max_step = n
            elif n['num'] == max_step['num'] and (max_step['end'] - max_step['start']) > (n['end'] - n['start']):
                max_step = n

        return max_step['end'] - max_step['start'] + 1


slu = Solution()
print(slu.findShortestSubArray([1, 2, 2, 3, 1]))
