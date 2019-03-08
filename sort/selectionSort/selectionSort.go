package main

import "fmt"

func selectionSort(arr []int) []int {
	len := len(arr)
	for i := 1; i <= len-1; i++ {
		maxIndex := 0
		for j := 0; j <= len-i; j++ {
			if arr[maxIndex] < arr[j] {
				maxIndex = j
			}
		}
		// swap indexnum
		tmpValue := arr[len-i]
		arr[len-i] = arr[maxIndex]
		arr[maxIndex] = tmpValue
	}
	return arr
}

func main() {
	arr := []int{10, 1, 9, 2, 8, 3, 7, 4, 6, 5}

	fmt.Println(selectionSort(arr))

}
