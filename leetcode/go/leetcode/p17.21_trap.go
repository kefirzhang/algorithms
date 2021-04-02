package leetcode

func trap(height []int) int {
	n := len(height)
	if n <= 2 {
		return 0
	}
	left := make([]int, n)
	right := make([]int, n)
	left[0] = 0
	right[n-1] = 0
	maxLeft := 0
	maxRight := 0
	// 遍历获得当前位置左边最大的量
	for i := 0; i < n; i++ {
		if maxLeft < height[i] {
			maxLeft = height[i]
		}
		left[i] = maxLeft
	}
	for i := n - 1; i >= 0; i-- {
		if maxRight < height[i] {
			maxRight = height[i]
		}
		right[i] = maxRight
	}
	//遍历右边的

	//遍历 然后获得当前最大的 面积 累计 就返回最大的
	area := 0
	for i := 1; i < n-1; i++ {
		if height[i] < left[i-1] && height[i] < right[i+1] {
			area = area + absDiff(left[i-1]-height[i], right[i+1]-height[i])
		}
	}

	return area
}

func absDiff(a, b int) int {
	if a <= b {
		return a
	} else {
		return b
	}
}
