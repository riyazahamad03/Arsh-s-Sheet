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
    def middleNode(self, head: Node):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.val


Lnode = LinkedList()
Lnode.add(1)
Lnode.add(2)
Lnode.add(3)
Lnode.add(4)
Lnode.add(5)


x = solution()
print(x.middleNode(Lnode.head))
