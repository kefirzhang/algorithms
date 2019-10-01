import queue

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.helper_data_1 = queue.Queue()
        self.helper_data_2 = queue.Queue()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.helper_data_2.put(x)
        while not self.helper_data_1.empty():
            self.helper_data_2.put(self.helper_data_1.get())

        self.helper_data_1 = self.helper_data_2
        self.helper_data_2 = queue.Queue()

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.helper_data_1.get()

    def top(self) -> int:
        """
        Get the top element.
        """
        tmp = self.helper_data_1.get()
        if tmp:
            self.push(tmp)
        return tmp

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.helper_data_1.empty()


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()
print(param_2, param_3, param_4)
