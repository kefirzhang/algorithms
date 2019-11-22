package main

import "fmt"

func twoSum(nums []int, target int) [][]int {
	var ret [][]int
	var numsMap map[int][]int
	numsMap = make(map[int][]int)

	for i := 0; i < len(nums); i += 1 {
		_, ok := numsMap [nums[i]]
		if ok {
			numsMap[nums[i]] = append(numsMap[nums[i]], i)
		} else {
			tmpSlice := []int{i}
			numsMap[nums[i]] = tmpSlice
		}
	}

	for i := 0; i < len(nums); i += 1 {
		curTarget := target - nums[i]
		combineTarget, ok := numsMap[curTarget]
		if ok {
			for j := 0; j < len(combineTarget); j += 1 {
				if i == combineTarget[j] {
					continue
				} else {
					combine := [] int{nums[i], curTarget}
					ret = append(ret, combine)
				}
			}
		}
	}
	return ret
}

func threeSum(nums []int) [][]int {
	var ret [][]int
	ret = append(ret, nums)
	return ret
}
func main() {
	nums := [] int{-1, 0, 1, 2, -1, -4, 4}
	ret := twoSum(nums, 0)
	fmt.Print(ret)
}

// nums = [-1, 0, 1, 2, -1, -4]
