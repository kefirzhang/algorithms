package main

import "fmt"

func shellSort(arr []int) []int {
	n := len(arr)

	for gap := n / 2; gap > 0; gap = gap / 2 {
		for i := gap; i < n; i++ {
			for j := i; (j-gap) >= 0 && arr[j] < arr[j-gap]; j -= gap {
				tmp := arr[j-gap]
				arr[j-gap] = arr[j]
				arr[j] = tmp
			}
		}
	}
	return arr
}

func main() {
	arr := []int{10, 1, 9, 2, 8, 3, 7, 4, 6, 5}
	fmt.Println(shellSort(arr))
}
