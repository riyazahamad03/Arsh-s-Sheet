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


class Solution:
    def rearrange(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        node = head
        is_greater = True

        while node.next != None:
            if is_greater:
                if node.val > node.next.val:
                    t = node.val
                    node.val = node.next.val
                    node.next.val = t
            else:
                if node.next.next != None and node.next.val < node.next.next.val:
                    t = node.next.val
                    node.next.val = node.next.next.val
                    node.next.next.val = t
                node = node.next
            is_greater = not is_greater

        return head


x = Solution()
rearranged_head = x.rearrange(l1.head)


current = rearranged_head
while current:
    print(current.val, end=" -> ")
    current = current.next
