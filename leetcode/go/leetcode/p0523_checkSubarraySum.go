package leetcode

func checkSubarraySum(nums []int, k int) bool {
	m := make(map[int]int)
	m[0] = -1
	sum := 0
	if len(nums) < 2 {
		return false
	}
	for i, num := range nums {
		sum += num
		if k != 0 {
			sum %= k
		}
		if _, ok := m[sum]; ok {
			if i-m[sum] > 1 {
				return true
			}
		} else {
			m[sum] = i
		}
	}
	return false
}
