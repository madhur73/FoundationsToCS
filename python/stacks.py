from collections import deque


class MyStack:
    def __init__(self):
        self.stack = deque()

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        try:
            val = self.stack.pop()
            return val
        except:
            print("Stack is empty")


class MyQueue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, val):
        self.queue.append(val)

    def dequeue(self):
        try:
            val = self.queue.pop()
            return val
        except:
            print("Empty Quque Dequeu operaiton")


s = MyQueue()
s.dequeue()
# s.push(1)
# s.push(2)
# s.pop()
