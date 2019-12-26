from collections import OrderedDict


class LRUCache2(OrderedDict):

    def __init__(self, capacity: int):
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)


class DLinkedNode:
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None


class LRUCache:
    def _add_node(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        prev = node.prev
        new = node.next

        prev.next = new
        new.prev = prev

    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        res = self.tail.prev
        self._remove_node(res)
        return res

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.size = 0
        self.head, self.tail = DLinkedNode(), DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        node = self.cache.get(key, None)
        if not node:
            return -1
        self._move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        if not node:
            new_node = DLinkedNode()
            new_node.key = key
            new_node.value = value
            self.cache[key] = new_node
            self._add_node(new_node)
            self.size += 1
            if self.size > self.capacity:
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            node.value = value
            self._move_to_head(node)


# Your LRUCache object will be instantiated and called as such:
cache = LRUCache(2)

cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))  # 返回  1
cache.put(3, 3)  # 该操作会使得密钥 2 作废
print(cache.get(2))  # 返回 -1 (未找到)
cache.put(4, 4)  # 该操作会使得密钥 1 作废
print(cache.get(1))  # 返回 -1 (未找到)
print(cache.get(3))  # 返回  3
print(cache.get(4))  # 返回  4
