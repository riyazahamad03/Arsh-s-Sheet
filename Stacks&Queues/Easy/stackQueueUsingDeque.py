class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        if self.head == None:
            return True
        return False

    def insertFirst(self, x: int):
        ptr = Node(x)
        if self.head == None:
            self.head = self.tail = ptr
        else:
            ptr.next = self.head
            self.head.prev = ptr
            self.head = ptr

    def insertLast(self, x: int):
        ptr = Node(x)
        if self.head == None:
            self.head = self.tail = ptr
        else:
            ptr.prev = self.tail
            self.tail.next = ptr
            self.tail = ptr

    def size(self):
        Len = 0
        curr = self.head
        while curr:
            Len += 1
            curr = curr.next
        return Len

    def removeFirst(self):
        if not self.isEmpty():
            self.head = self.head.next
            if self.head != None:
                self.head.prev = None

    def removeLast(Self):
        if not Self.isEmpty():
            Self.tail = Self.tail.prev
            if Self.tail != None:
                Self.tail.next = None

    def display(self):
        if self.isEmpty():
            return "List Is Empty"
        curr = self.head
        while curr:
            print(curr.val, end=" ")
            curr = curr.next


class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self, elem):
        self.stack.insertLast(elem)

    def pop(self):
        self.stack.removeLast()

    def size(self):
        self.stack.size()

    def display(self):
        self.stack.display()


class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, elem):
        self.queue.insertLast(elem)

    def dequeue(self):
        self.queue.removeFirst()

    def size(self):
        self.queue.size()

    def display(self):
        self.queue.display()


stk = Stack()

# push 7 and 8 at top of stack
stk.push(7)
stk.push(8)
print("Stack: ")
stk.display()

# pop an element
stk.pop()
print("Stack: ")
stk.display()

# Object of Queue
que = Queue()

# Insert 12 and 13 in queue
que.enqueue(12)
que.enqueue(13)
print("Queue: ")
que.display()

# Delete an element from queue
que.dequeue()
print("Queue: ")
que.display()

print("Size of stack is ", stk.size())
print("Size of queue is ", que.size())
