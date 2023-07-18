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
    def deleteDuplicate(self, head: ListNode):
        dummy = ListNode(0, head)
        curr = dummy.next
        prev = dummy
        while curr:
            if curr.next and curr.next.val == curr.val:
                while curr.next and curr.next.val == curr.val:
                    curr = curr.next
                prev.next = curr.next
            else:
                prev = prev.next
            curr = curr.next
        return dummy.next


l1 = LinkedList()
l1.add(1)
l1.add(2)
l1.add(3)
l1.add(4)
l1.add(5)

x = solution()
print(x.deleteDuplicate(l1.head))
