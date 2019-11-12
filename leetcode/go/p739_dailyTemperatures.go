package main

import "fmt"

func dailyTemperatures(T []int) []int {
	length := len(T)
	var ret []int
	for i := 0; i < length; i += 1 {
		distance := 0
		for j := i + 1; j < length; j += 1 {
			if T[j] > T[i] {
				distance = j - i
				break
			}
		}
		ret = append(ret, distance)
	}
	return ret
}

func main() {
	T := []int{73, 74, 75, 71, 69, 72, 76, 73}
	ret := dailyTemperatures(T)
	fmt.Print(ret)

}
