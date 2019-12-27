class Solution:
    def leastInterval(self, tasks, n: int) -> int:
        helper = {}
        max_num = 0
        for i in tasks:
            if helper.__contains__(i):
                helper[i] += 1
            else:
                helper[i] = 1
            max_num = max(max_num, helper[i])
        max_times = 0
        for i in helper:
            if helper[i] == max_num:
                max_times += 1

        min_step = (max_num - 1) * (n + 1) + max_times
        if min_step < len(tasks):
            min_step = len(tasks)
        return min_step


slu = Solution()
print(slu.leastInterval(["A", "A", "A", "B", "B", "B"],2))
