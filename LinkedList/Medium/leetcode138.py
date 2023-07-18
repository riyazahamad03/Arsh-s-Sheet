class Node:
    def __init__(self, val, random=None):
        self.val = val
        self.random = random
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.Length = 0

    def add(self, data, rand):
        newNode = Node(data, rand)
        if self.head == None:
            self.head = newNode
            self.tail = self.head
        else:
            self.tail.next = newNode
            self.tail = newNode

        self.Length += 1


class solution:
    def copyRandomPointer(self, head: Node):
        hashMap = {None: None}
        curr = head
        # storing in hashMap
        while curr:
            copy = Node(curr.val)
            hashMap[curr] = copy
            curr = curr.next

        # assining pointer references
        curr = head
        while curr:
            copy = hashMap[curr]
            copy.next = hashMap[curr.next]
            copy.random = hashMap[curr.random]

            curr = curr.next
        return hashMap[head]


l1 = LinkedList()
node1 = Node(7)
node2 = Node(13)
node3 = Node(11)
node4 = Node(10)
node5 = Node(1)

l1.head = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

node1.random = None
node2.random = node1
node3.random = node5
node4.random = node3
node5.random = node1

x = solution()
print(x.copyRandomPointer(l1.head))
