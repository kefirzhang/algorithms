package main

import "fmt"

func mergeSort(arr []int) []int {

	// 基线条件
	if len(arr) <= 1 {
		return arr
	}
	// 切分成两份

	var middleIndex = len(arr) / 2
	leftData := mergeSort(arr[middleIndex:])
	rightData := mergeSort(arr[:middleIndex])
	// 递归条件
	var sortedData []int
	for (len(leftData) > 0 && len(rightData) > 0) {
		if (leftData[0] <= rightData[0]) {
			sortedData = append(sortedData, leftData[0])
			leftData = leftData[1:]
		} else {
			sortedData = append(sortedData, rightData[0])
			rightData = rightData[1:]
		}
	}

	if (len(leftData) > 0) {
		sortedData = append(sortedData, leftData...)
	}
	if (len(rightData) > 0) {
		sortedData = append(sortedData, rightData...)
	}

	return sortedData
}

func main() {
	var unSortedData = []int{10, 1, 9, 2, 8, 3, 7, 4, 6, 5}
	var sortedData = mergeSort(unSortedData)
	fmt.Println(sortedData)
}
