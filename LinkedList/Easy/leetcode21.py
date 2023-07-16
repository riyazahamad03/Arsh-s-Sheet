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
    def mergeTwoList(self, l1: Node, l2: Node):
        resNode = Node(0)
        tailNode = resNode
        while l1 and l2:
            if l1.val < l2.val:
                tailNode.next = l1
                l1 = l1.next
            else:
                tailNode.next = l2
                l2 = l2.next
            tailNode = tailNode.next
        if l1:
            tailNode.next = l1
        if l2:
            tailNode.next = l2
        return resNode.next


fNode = LinkedList()
fNode.add(1)
fNode.add(1)
fNode.add(2)


sNode = LinkedList()
sNode.add(0)
sNode.add(3)
sNode.add(5)


ans = solution()
print(ans.mergeTwoList(fNode.head, sNode.head))


while ans:
    print(ans.val)
    ans = ans.next
