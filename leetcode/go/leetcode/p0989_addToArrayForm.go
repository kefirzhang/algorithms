package leetcode

func addToArrayForm(A []int, K int) []int {
	var s []int
	n := len(A)
	i := n - 1
	for K > 0 && i >= 0 {
		K += A[i]
		s = append(s, K%10)
		K /= 10
		i--
	}
	for i >= 0 {
		s = append(s, A[i])
		i--
	}
	for K > 0 {
		s = append(s, K%10)
		K = K / 10
	}
	for l, r := 0, len(s)-1; l < r; {
		s[l], s[r] = s[r], s[l]
		l++
		r--
	}
	return s
}
