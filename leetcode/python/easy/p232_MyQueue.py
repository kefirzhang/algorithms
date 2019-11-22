class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack2.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.stack1) == 0:
            while len(self.stack2) > 0:
                self.stack1.append(self.stack2.pop())

        return self.stack1.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.stack1) == 0:
            while len(self.stack2) > 0:
                self.stack1.append(self.stack2.pop())

        return self.stack1[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if len(self.stack1) == 0:
            while len(self.stack2) > 0:
                self.stack1.append(self.stack2.pop())

        return len(self.stack1) == 0


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)

param_1 = obj.peek()
param_2 = obj.pop()
param_3 = obj.empty()
print(param_1, param_2, param_3)

