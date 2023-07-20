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


l1 = LinkedList()
l1.add(1)
l1.add(0)
l1.add(0)

l2 = LinkedList()
l2.add(1)
l2.add(0)


class solution:
    def subract(self, l1, l2):
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)

        dummy = ListNode(0)
        curr = dummy

        borrow = 0
        while l1 or l2 or borrow:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            diff = borrow + val1 - val2

            if diff < 0:
                borrow = -1
                diff += 10
            else:
                borrow = 0

            curr.next = ListNode(diff)
            curr = curr.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return self.reverse(dummy.next)

    def reverse(self, node):
        prev = None
        while node:
            tmp = node.next
            node.next = prev
            prev = node

            node = tmp
        return prev


x = solution()
node = x.subract(l1.head, l2.head)
while node != None:
    if node.next:
        print(node.val, end="->")
    else:
        print(node.val)
    node = node.next
