class Solution:
    def twoSum(self, numbers, target):
        length = len(numbers)
        if length <= 1:
            return []
        start = 0
        end = length - 1

        while numbers[start] + numbers[end] != target:
            if start >= end:
                return []
                break
            if numbers[start] + numbers[end] < target:
                start += 1
            else:
                end -= 1

        return [start + 1, end + 1]


slu = Solution()
print(slu.twoSum([2, 7, 11, 15], 9))
# numbers = [2, 7, 11, 15], target = 9
