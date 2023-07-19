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
l1.add(15)
l1.add(10)
l1.add(5)
l1.add(20)
l1.add(3)
l1.add(2)


class solution:
    def reverseKgroup(self, head: ListNode, k: int):
        dummy = ListNode(0, head)
        groupPrev = dummy
        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next
            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr

                curr = tmp

            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        return dummy.next
    def getKth(self, curr, k):
        while curr and k > 0:
            k -= 1
            curr = curr.next
        return curr


x = solution()
print(x.reverseKgroup(l1.head, 2))
