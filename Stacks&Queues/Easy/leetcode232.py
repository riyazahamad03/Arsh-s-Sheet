class MyQueue:
    def __init__(self) -> None:
        self.s1 = []
        self.s2 = []

    def push(self, x: int):
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while self.s2:
            self.s1.append(self.s2.pop())

    def pop(self):
        if self.s1:
            return self.s1.pop()

    def peek(self):
        return self.s1[-1]

    def empty(self):
        return len(self.s1) == 0


x = MyQueue()
x.push(1)
x.push(2)
x.peek()
x.pop()
