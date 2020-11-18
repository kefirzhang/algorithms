package leetcode

import (
	"fmt"
	"testing"
)

//不使用运算符 + 和 - ​​​​​​​，计算两整数 ​​​​​​​a 、b ​​​​​​​之和。
func TestGetSum(t *testing.T) {
	units := [][]int{{1, 2, 3}, {1, 3, 4}, {1, 4, 5}, {-1, 2, 1}}
	for _, unit := range units {
		if getSum(unit[0], unit[1]) == unit[2] {
			fmt.Println(unit, "PASS")
		} else {
			fmt.Println(unit, "Failing")
		}
	}
}
