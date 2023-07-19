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
    def rearrange(self, head: ListNode):
        node = head
        fast, slow = node, node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        node1, node2 = head, slow.next
        slow.next = None
        node2 = self.reverse(node2)

        dummy = ListNode(0)
        curr = dummy

        while node1 and node2:
            if node1:
                curr.next = node1
                curr = curr.next
                node1 = node1.next
            if node2:
                curr.next = node2
                curr = curr.next
                node2 = node2.next

        if node1:
            curr.next = node1
        if node2:
            curr.next = node2
        return dummy.next

    def reverse(self, node):
        prev = None
        curr = node
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr

            curr = tmp
        return prev


l1 = LinkedList()
l1.add(1)
l1.add(2)
l1.add(3)
l1.add(4)
l1.add(5)

x = solution()
newNode = x.rearrange(l1.head)
while newNode:
    print(newNode.val, end=" ")
    newNode = newNode.next
