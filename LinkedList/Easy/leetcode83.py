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
    def deleteDuplicate(self, head: Node):
        curr = head
        while curr:
            if curr.next and curr.next.val == curr.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head


Lnode = LinkedList()
Lnode.add(1)
Lnode.add(1)
Lnode.add(2)

x = solution()
print(x.deleteDuplicate(Lnode.head))
