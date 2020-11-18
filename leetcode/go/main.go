package main

import "fmt"

func missingNumber(nums []int) int {
	n := len(nums)
	total := ((n + 1) * n) / 2
	for _, num := range nums {
		total -= num
	}
	return total
}

func main() {
	nums := []int{0, 1}
	fmt.Println(missingNumber(nums))
}
