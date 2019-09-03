class Solution:
    def rotate(self, nums, k):
        length = len(nums)
        if k >= length:
            k = k % length
        if k == 0:
            return
        cur_loop = 0  # 循环标记
        pre = nums[cur_loop]
        cur_idx = cur_loop + k
        step =0
        while step < length:
            old = nums[cur_idx]
            nums[cur_idx] = pre
            pre = old
            if cur_idx == cur_loop:  # 转了一圈 换了一圈
                cur_loop += 1
                cur_idx = cur_loop
                pre = nums[cur_idx]
            cur_idx += k
            if cur_idx >= length:
                cur_idx -= length

            step += 1


slu = Solution()
print(slu.rotate([1, 2, 3, 4, 5, 6], 7))
