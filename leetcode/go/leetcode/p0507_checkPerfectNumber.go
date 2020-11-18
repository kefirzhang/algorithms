package leetcode

import (
	"math"
)

func checkPerfectNumber(num int) bool {
	if num < 4 {
		return false
	}
	sum := 1
	base := int(math.Sqrt(float64(num)))
	for i := 2; i <= base; i++ {
		if num%i == 0 {
			if i*i == num {
				sum += i
			} else {
				sum += i
				sum += num / i
			}
		}
	}
	return sum == num
}
