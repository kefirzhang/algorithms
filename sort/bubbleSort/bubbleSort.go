package main

import "fmt"

func bubbleSort(arr []int) []int {
	len := len(arr)
	for i := 1; i <= len-1; i++ {
		for j := 0; j <= len-1-i; j++ {
			if arr[j] > arr[j+1] {
				tmp := arr[j+1]
				arr[j+1] = arr[j]
				arr[j] = tmp
			}

		}
	}
	return arr
}


func main() {
	arr := []int{10,1,9,2,8,3,7,4,6,5}
	fmt.Println(bubbleSort(arr))
}
