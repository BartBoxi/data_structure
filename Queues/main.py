# # Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).
# #
# # Implement the MyStack class:
# #
# # void push(int x) Pushes element x to the top of the stack.
# # int pop() Removes the element on the top of the stack and returns it.
# # int top() Returns the element on the top of the stack.
# # boolean empty() Returns true if the stack is empty, false otherwise.
# # Notes:
# #
# # You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
# # Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.
# #
# #
# # Example 1:
# #
# # Input
# # ["MyStack", "push", "push", "top", "pop", "empty"]
# # [[], [1], [2], [], [], []]
# # Output
# # [null, null, null, 2, 2, false]
# #
# # Explanation
# # MyStack myStack = new MyStack();
# # myStack.push(1);
# # myStack.push(2);
# # myStack.top(); // return 2
# # myStack.pop(); // return 2
# # myStack.empty(); // return False
# #
# #
# # Constraints:
# #
# # 1 <= x <= 9
# # At most 100 calls will be made to push, pop, top, and empty.
# # All the calls to pop and top are valid.
# #
# #
# # Follow-up: Can you implement the stack using only one queue?
#
# #implementation of the queue using collection.deque
# # from collections import deque
# #
# # qu = [1,2,3,4]
# #
# # class Queue:
# #     def __init__(self):
# #         self._elements = deque()
# #
# #     def enqueue(self, element):
# #         self._elements.append(element)
# #
# #     def dequeue(self):
# #         return self._elements.popleft()
# #
# #
# # def test_queue():
# #     q = Queue()
# #
# #     q.enqueue(21)
# #     q.enqueue(1)
# #     q.enqueue(7)
# #     q.enqueue(2)
# #
# #     print(q.dequeue())
# #     print(q.dequeue())
# #
# # test_queue()
#
# ### test on how to implement a stack using a queue
#
# from collections import deque
# #
# # class StackUsingQueues:
# #     def __init__(self):
# #         self.queue1 = deque()
# #         self.queue2 = deque()
# #
# #     def push(self, element):
# #         self.queue2.append(element)
#
#
# # q1 = deque()
# # q2 = deque()
# #
# # q2.append('a')
# # q1.append(q2.pop())
# #
# #
# #
# # q2.append('sd')
# # q1.append(q2.pop())
# #
# # q2.append('f')
# # q1.append(q2.pop())
# #
# # print(q2)
# # print(q1)
# # print(q1.pop())
#
# q1 = deque()
#
# q1.append(1)
# q1.append(2)
# q1.append(3)
# q1.append(3112)
# q1.append(332)
# q1.append(23)
# q1.append(5)
# print(q1)
#
# q2 = deque()
#
#
# q2.append(q1.pop())
# print(q2)
#
#
#
# # class stack:
# #
# #     def __init__(self):
# #         self.q1 = deque()
# #         self.q2 = deque()
# #
# #     def push(self, x: int):
# #         q2 = self.q2.append(x)
# #         while self.q1:



