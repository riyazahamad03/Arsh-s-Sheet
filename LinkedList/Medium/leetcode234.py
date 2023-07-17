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
    def isPalindrome(self, head: ListNode):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow:
            nxtSlow = slow.next
            slow.next = prev
            prev = slow

            slow = nxtSlow

        left, right = head, prev

        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True


l1 = LinkedList()
l1.add(1)
l1.add(2)
l1.add(1)

x = solution()
print(x.isPalindrome(l1.head))
