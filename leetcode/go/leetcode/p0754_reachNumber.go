package leetcode

import (
	"math"
)

func reachNumber(target int) int {
	target = int(math.Abs(float64(target)))
	step := 0
	sum := 0
	for i := 1; i <= target; i++ {
		step++
		sum += i
		if sum >= target {
			if sum == target || (sum-target)%2 == 0 {

			} else {
				if step%2 == 0 {
					step += 1
				} else {
					step += 2
				}
			}
			break
		}
	}
	return step
}
