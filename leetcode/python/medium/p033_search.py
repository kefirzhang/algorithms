class Solution:
    def search(self, nums, target: int) -> int:
        def find_rotate_index(start, end):
            if nums[start] < nums[end]:
                return 0
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] > nums[mid + 1]:
                    return mid + 1
                else:
                    if nums[mid] < nums[start]:
                        end = mid - 1
                    else:
                        start = mid + 1
            return 0

        def binary_search(start, end):

            while start <= end:
                mid = int((start + end) / 2)
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return -1

        n = len(nums)
        if n == 0:
            return -1
        if n == 1:
            return 0 if nums[0] == target else -1
        rotate_index = find_rotate_index(0, n - 1)
        # print(rotate_index)
        if nums[rotate_index] == target:
            return rotate_index
        left = binary_search(0, rotate_index - 1)
        right = binary_search(rotate_index, n - 1)
        # print(left, right)
        if left != -1:
            return left
        elif right != -1:
            return right
        else:
            return -1


slu = Solution()
print(slu.search([1,3], 1))
