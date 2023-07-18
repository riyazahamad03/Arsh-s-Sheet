class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        newNode = ListNode(data)
        if not self.head:
            self.head = newNode
            self.tail = self.head
        else:
            self.tail.next = newNode
            self.tail = newNode


class solution:
    def multiply(self, l1, l2):
        n1 = n2 = 0
        while l1:
            n1 = n1 * 10 + l1.val
            l1 = l1.next
        while l2:
            n2 = n2 * 10 + l2.val
            l2 = l2.next

        return n1 * n2


l1 = LinkedList()
l1.add(1)
l1.add(0)
l1.add(0)

l2 = LinkedList()
l2.add(1)
l2.add(0)

x = solution()
print(x.multiply(l1.head, l2.head))
