class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mod = 100
        self.data = [None] * self.mod

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        index = key % self.mod
        node = ListNode(key, value)
        node.next = self.data[index]
        self.data[index] = node

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        index = key % self.mod
        node = self.data[index]
        while node is not None:
            if node.key == key:
                return node.val
            node = node.next
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        index = key % self.mod
        head = node = ListNode(None,None)
        node.next = self.data[index]
        while node.next is not None:
            if node.next.key == key:
                node.next = node.next.next
            else:
                node = node.next
        self.data[index] = head.next


# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
obj.put(1, 2)
param_2 = obj.get(1)
print(param_2)
obj.remove(1)
param_2 = obj.get(1)
print(param_2)
