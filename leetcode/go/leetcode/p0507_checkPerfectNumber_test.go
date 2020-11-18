package leetcode

import (
	"fmt"
	"testing"
)

//不使用运算符 + 和 - ​​​​​​​，计算两整数 ​​​​​​​a 、b ​​​​​​​之和。
func TestCheckPerfectNumber(t *testing.T) {
	for i := 0; i <= 28; i++ {
		if checkPerfectNumber(i) {
			fmt.Println(i, "is perfect num")
		}
	}
}
