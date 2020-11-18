package leetcode

import "container/list"

func orangesRotting(grid [][]int) int {
	step := 0
	l := list.New()
	m, n := len(grid), len(grid[0])
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] == 2 {
				l.PushBack([]int{i, j})
			}
		}
	}
	md := []int{1, -1, 0, 0}
	nd := []int{0, 0, 1, -1}
	for l.Len() > 0 {
		ln := l.Len()
		for i := 0; i < ln; i++ {
			node := l.Front()
			for idx, _ := range md {
				r := node.Value.([]int)[0] + md[idx]
				c := node.Value.([]int)[1] + nd[idx]
				if r >= 0 && r < m && c >= 0 && c < n && grid[r][c] == 1 {
					grid[r][c] = 2
					l.PushBack([]int{r, c})
				}
			}
			l.Remove(node)
		}
		if l.Len() > 0 {
			step++
		}
	}
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] == 1 {
				return -1
			}
		}
	}
	return step
}
