class Solution:
    def findDuplicate(self, nums) -> int:
        hare = nums[0]
        tortoise = nums[0]

        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        ptr1, ptr2 = nums[0], tortoise
        while ptr1 != ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]

        return ptr1


slu = Solution()
print(slu.findDuplicate([1, 3, 4, 2, 2]))
