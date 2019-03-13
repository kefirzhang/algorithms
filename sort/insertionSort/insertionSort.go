package main

import "fmt"

func insertionSort(arr []int) []int {
	n := len(arr)
	for i := 0; i < n; i++ {
		for j := i; j > 0  && arr[j] < arr[j-1]; j-- {
			tmp := arr[j-1]
			arr[j-1] = arr[j]
			arr[j] = tmp
		}
	}
	return arr
}

func main() {
	arr := []int{10, 1, 9, 2, 8, 3, 7, 4, 6, 5}
	fmt.Println(insertionSort(arr))
}


