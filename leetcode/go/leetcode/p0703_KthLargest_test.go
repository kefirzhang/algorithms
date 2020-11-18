package leetcode

import (
	"fmt"
	"testing"
)

func TestKthLargest(t *testing.T) {
	obj := Constructor(3, []int{4, 5, 8, 2})
	fmt.Println(obj.h)
	param := obj.Add(3)

	fmt.Println(param, obj.h)
	param = obj.Add(5)
	fmt.Println(param, obj.h)
	param = obj.Add(10)
	fmt.Println(param, obj.h)
	param = obj.Add(9)
	fmt.Println(param, obj.h)
	param = obj.Add(4)
	fmt.Println(param, obj.h)

}
