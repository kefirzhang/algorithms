class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mod = 100
        self.data = [None] * self.mod

    def add(self, key: int) -> None:
        index = key % self.mod
        node = ListNode(key)
        node.next = self.data[index]
        self.data[index] = node

    def remove(self, key: int) -> None:
        index = key % self.mod
        head = node = ListNode(None)
        node.next = self.data[index]
        while node.next is not None:
            if node.next.key == key:
                node.next = node.next.next
            else:
                node = node.next
        self.data[index] = head.next

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        index = key % self.mod
        node = self.data[index]
        while node is not None:
            if node.key == key:
                return True
            node = node.next
        return False


# Your MyHashSet object will be instantiated and called as such:
hashSet = MyHashSet();
hashSet.add(1)
hashSet.add(2)
print(hashSet.contains(1))  # 返回 true
print(hashSet.contains(3))  # 返回 false (未找到)
hashSet.add(2)
print(hashSet.contains(2))  # 返回 true
hashSet.remove(2)
print(hashSet.contains(2))  # 返回  false (已经被删除)
