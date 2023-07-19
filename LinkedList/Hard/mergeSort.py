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
    def mergeSort(self, head):
        if head is None or head.next is None:
            return head

        mid = self.getMiddle(head)
        midNxt = mid.next
        mid.next = None

        left = self.mergeSort(head)
        right = self.mergeSort(midNxt)

        res = self.merge(left, right)
        return res

    def merge(self, left, right):
        dummy = ListNode(0)
        curr = dummy
        while left and right:
            if left.val <= right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next

        if left:
            curr.next = left
        elif right:
            curr.next = right

        return dummy.next

    def getMiddle(self, node):
        if node == None or node.next == None:
            return node

        slow = node
        fast = node.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


l1 = LinkedList()
l1.add(15)
l1.add(10)
l1.add(5)
l1.add(20)
l1.add(3)
l1.add(2)

x = Solution()
X = x.mergeSort(l1.head)
while X:
    print(X.val, end=" ")
    X = X.next
