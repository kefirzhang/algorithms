package main

import "fmt"

//自定义一个quickSort的方法
// 需要逐步优化  go 还是不是很熟悉
func quickSort(arr []int) []int {
	//基准条件
	if (len(arr) <= 1) {
		return arr
	}
	//递归条件 随机选择一个函数 然后 拆分数组
	var pickKey = 0
	var pickValue = arr[pickKey]
	var smallerData []int
	var biggerData []int
	var sortedData []int
	for i, v:= range arr {
		if(i != pickKey) {
			if(v <= pickValue) {
				smallerData = append(smallerData,v)
			}else {
				biggerData = append(biggerData,v)
			}
		}
	}
	smallerData = quickSort(smallerData)
	biggerData = quickSort(biggerData)
	smallerData = append(smallerData,pickValue)
	sortedData = append(smallerData,biggerData...)
	return sortedData
}

func main() {
	// 初始化一个随机数组
	//var unSortedData [10] int
	var unSortedData = []int{10, 1, 9, 2, 8, 3, 7, 4, 6, 5}
	var sortedData = quickSort(unSortedData)
	// 调用快排方法
	// 打印结果
	fmt.Println(sortedData)
}
