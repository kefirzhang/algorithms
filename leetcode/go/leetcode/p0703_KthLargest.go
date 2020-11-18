package leetcode

import (
	"container/heap"
	"sort"
)

// An IntHeap is a min-heap of ints.
type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *IntHeap) Push(x interface{}) {
	// Push and Pop use pointer receivers because they modify the slice's length,
	// not just its contents.
	*h = append(*h, x.(int))
}

func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

type KthLargest struct {
	k int
	h *IntHeap
}

func Constructor(k int, nums []int) KthLargest {
	sort.Sort(IntHeap(nums))
	if len(nums) > k {
		nums = nums[len(nums)-k:]
	}
	h := IntHeap(nums)
	heap.Init(&h)
	return KthLargest{k, &h}

}

func (this *KthLargest) Add(val int) int {
	if this.h.Len() < this.k {
		heap.Push(this.h, val)
		return (*this.h)[0]
	}
	if val > (*this.h)[0] {
		(*this.h)[0] = val
		heap.Fix(this.h, 0)
		return (*this.h)[0]
	}
	return (*this.h)[0]
}
