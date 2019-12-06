class Solution:
    def __init__(self):
        self.res = []
    def permute(self, nums):
        self.backTrack(nums, [])
        return self.res

    def backTrack(self, nums, track):
        if len(nums) == len(track):
            self.res.append(track[:])
            return
        for i in nums:
            if i in track:
                continue
            track.append(i)
            self.backTrack(nums, track)
            track.remove(i)


slu = Solution()
print(slu.permute([1]))
