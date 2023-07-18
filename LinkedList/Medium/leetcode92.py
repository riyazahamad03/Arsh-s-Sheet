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
    def reverseBetween(self, head: ListNode, left: int, right: int):
        dummy = ListNode(0, head)

        lftPrev, curr = dummy, head
        for i in range(left - 1):
            lftPrev.next = curr
            curr = curr.next

        prv = None
        for i in range(right - left + 1):
            tmp = curr.next
            curr.next = prv
            prv = curr

            curr = tmp

        lftPrev.next.next = curr
        lftPrev.next = prv
        return dummy.next


l1 = LinkedList()
l1.add(1)
l1.add(2)
l1.add(3)
l1.add(4)
l1.add(5)
l1.add(6)


x = solution()
print(x.reverseBetween(l1.head, 2, 4))
