class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        s1, s2 = [], []

        while l1:
            s1.append(l1.val)
            l1 = l1.next

        while l2:
            s2.append(l2.val)
            l2 = l2.next

        Sum, carry = 0, 0
        ans = ListNode(0)

        while s1 or s2:
            if s1:
                Sum += s1.pop()
            if s2:
                Sum += s2.pop()

            carry = Sum//10
            value = Sum % 10

            ans.val = value
            head = ListNode(carry)
            head.next = ans
            ans = head

            Sum = carry
        return ans.next if not carry else ans


l1 = LinkedList()
l1.add(1)
l1.add(4)
l1.add(5)


l2 = LinkedList()
l2.add(4)
l2.add(4)
l2.add(5)


x = solution()
print(x.addTwoNumbers(l1.head, l2.head))
