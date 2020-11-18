package leetcode

type Node struct {
	Val         bool
	IsLeaf      bool
	TopLeft     *Node
	TopRight    *Node
	BottomLeft  *Node
	BottomRight *Node
}

func intersect(quadTree1 *Node, quadTree2 *Node) *Node {
	if quadTree1.IsLeaf {
		if quadTree1.Val {
			return quadTree1
		} else {
			return quadTree2
		}
	}
	if quadTree2.IsLeaf {
		if quadTree2.Val {
			return quadTree2
		} else {
			return quadTree1
		}
	}
	topLeft := intersect(quadTree1.TopLeft, quadTree2.TopLeft)
	topRight := intersect(quadTree1.TopRight, quadTree2.TopRight)
	bottomLeft := intersect(quadTree1.BottomLeft, quadTree2.BottomLeft)
	bottomRight := intersect(quadTree1.BottomRight, quadTree2.BottomRight)
	if topLeft.IsLeaf && topLeft.Val && topRight.IsLeaf && topRight.Val && bottomLeft.IsLeaf && bottomLeft.Val && bottomRight.IsLeaf && bottomRight.Val {
		return &Node{true, true, nil, nil, nil, nil}
	}
	return &Node{false, false, topLeft, topRight, bottomLeft, bottomRight}

}
