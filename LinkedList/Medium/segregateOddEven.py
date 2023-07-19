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


class Solution:
    def segreGate(self, head):
        even_dummy = ListNode(0)
        odd_dummy = ListNode(0)
        even_tail = even_dummy
        odd_tail = odd_dummy

        current = head
        while current:
            if current.val % 2 == 0:
                even_tail.next = current
                even_tail = even_tail.next
            else:
                odd_tail.next = current
                odd_tail = odd_tail.next
            current = current.next

        even_tail.next = odd_dummy.next
        odd_tail.next = None

        return even_dummy.next


l1 = LinkedList()
l1.add(1)
l1.add(2)
l1.add(3)
l1.add(4)
l1.add(5)


x = Solution()
new = x.segreGate(l1.head)

while new:
    print(new.val, end=" ")
    new = new.next
