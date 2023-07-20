import collections


class MyStack:
    def __init__(self):
        self.q = collections.deque()

    def push(self, x: int):
        self.q.append(x)

    def pop(self):
        for i in range(len(self.q) - 1):
            self.push(self.q.popleft())
        return self.q.popleft()

    def top(self):
        return self.q[-1]

    def empty(self):
        return len(self.q) == 0


x = MyStack()
x.push(1)
x.push(2)
x.pop()
x.empty()
