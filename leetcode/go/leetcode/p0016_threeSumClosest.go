package leetcode

import (
	"math"
	"sort"
)

func threeSumClosest(nums []int, target int) int {
	ret := math.MaxInt32
	diff := math.MaxInt32
	sort.Ints(nums)
	n := len(nums)
	for i := 0; i < n-2; i++ {
		pl := i + 1
		pr := n - 1
		for pl < pr {
			sum := nums[i] + nums[pl] + nums[pr]
			if sum == target {
				return sum
			}
			if diff > int(math.Abs(float64(sum-target))) {
				ret = sum
				diff = int(math.Abs(float64(sum - target)))
			}
			if sum >= target {
				pr--
			} else {
				pl++
			}
		}
	}
	return ret
}
