package leetcode

func duplicateZerosPre(arr []int) {
	n := len(arr)
	for i := 0; i < n; i++ {
		if arr[i] == 0 {
			for j := n - 1; j > i; j-- {
				arr[j] = arr[j-1]
			}
			i++
		}
	}
}

func duplicateZeros(arr []int) {
	n := len(arr)
	mlen, midx := 0, 0

	for ; midx < n && mlen < n; midx++ {
		if arr[midx] == 0 {
			mlen += 2
		} else {
			mlen++
		}
	}
	for j := n - 1; j > 0 && midx > 0; j-- {
		if arr[midx-1] == 0 {
			if j == n-1 && mlen > n {
				arr[j] = 0
			} else {
				arr[j] = 0
				arr[j-1] = 0
				j--
			}
		} else {
			arr[j] = arr[midx-1]
		}
		midx--
	}
}
