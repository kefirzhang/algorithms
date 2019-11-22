class Solution:
    def merge(self, nums1, m, nums2, n) -> None:

        n_m = m - 1  # 指针
        n_n = n - 1  # 指针
        t_l = m + n - 1  # 数组总长度
        while n_m >= 0 and n_n >= 0:
            # print(t_l, n_m, n_n, nums1, nums2)
            if nums1[n_m] > nums2[n_n]:
                nums1[t_l] = nums1[n_m]
                n_m -= 1
            else:
                nums1[t_l] = nums2[n_n]
                n_n -= 1
            t_l -= 1
        while n_n >= 0:
            nums1[n_n] = nums2[n_n]
            n_n -= 1

        return nums1
        """
        Do not return anything, modify nums1 in-place instead.
        """


nums1 = [4, 5, 6, 0, 0, 0]
m = 3
nums2 = [1, 2, 3]
n = 3
slu = Solution()
print(slu.merge(nums1, m, nums2, n))
