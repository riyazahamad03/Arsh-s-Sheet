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
    def sortLinkedList(self, head: Node):
        node = Node(0)
        tail = node

        # 0's
        ptr = head
        while ptr:
            if ptr.val == 0:
                tail.next = Node(0)
                tail = tail.next
            ptr = ptr.next

        # 1's
        ptr = head
        while ptr:
            if ptr.val == 1:
                tail.next = Node(1)
                tail = tail.next
            ptr = ptr.next

        # 2's
        ptr = head
        while ptr:
            if ptr.val == 2:
                tail.next = Node(2)
                tail = tail.next
            ptr = ptr.next

        return node.next


Lnode = LinkedList()
Lnode.add(0)
Lnode.add(1)
Lnode.add(0)
Lnode.add(0)
Lnode.add(2)
Lnode.add(0)
Lnode.add(0)
Lnode.add(2)
Lnode.add(2)
Lnode.add(1)


x = solution()
vals = x.sortLinkedList(Lnode.head)

while vals:
    if vals.next:
        print(vals.val, end="->")
    else:
        print(vals.val, end="")
    vals = vals.next
