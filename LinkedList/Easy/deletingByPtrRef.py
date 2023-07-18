class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.Length = 0

    def add(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            self.tail = self.head
        else:
            self.tail.next = newNode
            self.tail = newNode

        self.Length += 1


class solution:
    def ptrRef(self, ptr):
        ptr.next = ptr.next.next


l1 = LinkedList()
l1.add(1)
l1.add(2)
l1.add(3)
l1.add(6)

p = l1.head
while p:
    print(p.val, end=" ")
    p = p.next
print()

ptr = l1.head.next
x = solution()
ans = x.ptrRef(ptr)

p = l1.head
while p:
    print(p.val, end=" ")
    p = p.next
