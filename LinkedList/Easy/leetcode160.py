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
    def getInterSectionPoint(self, headA: Node, headB: Node):
        l1, l2 = headA, headB
        while l1 and l2 and l1.val != l2.val:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA
        return l1.val if l1 else None


fNode = LinkedList()
fNode.add(1)
fNode.add(2)
fNode.add(3)

sNode = LinkedList()
sNode.add(4)
sNode.add(2)
sNode.add(2)



x = solution()
print(x.getInterSectionPoint(fNode.head, sNode.head))
