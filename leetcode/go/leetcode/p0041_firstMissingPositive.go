package leetcode

import "sort"

func firstMissingPositivePre1(nums []int) int {
	if len(nums) <= 0 {
		return 1
	}
	sort.Ints(nums)
	if nums[0] > 1 {
		return 1
	}
	n := len(nums)
	if nums[n-1] <= 0 {
		return 1
	}
	for i := 0; i < n-1; i++ {
		if nums[i] <= 0 {
			nums[i] = 0
		}
		if nums[i]+1 < nums[i+1] {
			return nums[i] + 1
		}
	}
	return nums[n-1] + 1
}

func firstMissingPositivePre2(nums []int) int {
	base := 1

	for _, v := range nums {
		if v <= 0 {
			continue
		}
		if v == base {
			base += 1
		}
	}
	return base
}

// 你可以实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案吗？

func hasValue(m map[int]bool, key int) bool {
	if _, ok := m[key]; ok {
		return true
	}
	return false
}

func firstMissingPositivePre3(nums []int) int {
	m := make(map[int]bool, len(nums))
	base := 1
	for _, v := range nums {
		if v <= 0 {
			continue
		}
		if base == v {
			base += 1
			for {
				if _, ok := m[base]; ok {
					base += 1
				} else {
					break
				}
			}
		}
		m[v] = true
	}
	return base
}

func firstMissingPositivePre4(nums []int) int {
	m := make(map[int]bool, len(nums))
	for _, v := range nums {
		m[v] = true
	}
	base := 1
	for {
		if _, ok := m[base]; ok {
			base += 1
		} else {
			break
		}
	}
	return base
}

func firstMissingPositive(nums []int) int {
	n := len(nums)
	for i := 0; i < n; i++ {
		for nums[i] > 0 && nums[i] <= n && nums[nums[i]-1] != nums[i] {
			nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
		}
	}
	for i := 0; i < n; i++ {
		if nums[i] != i+1 {
			return i + 1
		}
	}
	return n + 1
}
