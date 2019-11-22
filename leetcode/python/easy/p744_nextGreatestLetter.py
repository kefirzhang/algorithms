class Solution:
    def nextGreatestLetter(self, letters, target) -> str:
        if target < letters[0] or target >= letters[-1]:
            return letters[0]
        import math
        start = 0
        end = len(letters) - 1
        middle = math.ceil((start + end) / 2)
        while (letters[middle] > target >= letters[middle - 1]) is False:
            if letters[middle] > target:
                end = middle
            else:
                start = middle
            middle = math.ceil((start + end) / 2)
        return letters[middle]


slu = Solution()
print(slu.nextGreatestLetter(["c", "f", "j"], 'c'))
