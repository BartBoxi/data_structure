from collections import deque


class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        q2 = self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        if self.empty():
            raise IndexError("Pop from empty stack")
        return self.q1.popleft()  # pop left removes the element from the top

    def top(self) -> int:
        if self.empty():
            raise IndexError("Top from empty stack")
        return self.q1[0]

    def empty(self) -> bool:
        return not self.q1

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

# This is the solution i used