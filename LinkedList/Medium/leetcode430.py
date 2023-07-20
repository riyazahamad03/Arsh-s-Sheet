class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


# Creating the nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)
node9 = Node(9)
node10 = Node(10)

# Building the linked list
node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2
node3.next = node4
node4.prev = node3
node4.next = node5
node5.prev = node4

# Connecting child nodes
node3.child = node6
node6.next = node7
node7.prev = node6
node7.next = node8
node8.prev = node7

node8.child = node9
node9.next = node10
node10.prev = node9


class solution:
    def flatten(self, head):
        start = head
        stack = []
        while head:
            if head.child:
                if head.next:
                    stack.append(head.next)
                head.next = head.child
                head.next.prev = head
                head.child = None
            if head.next == None and len(stack) != 0:
                head.next = stack.pop()
                head.next.prev = head
            head = head.next

        return start


x = solution()
node = x.flatten(node1)


while node:
    print(node.val, end=" ")
    node = node.next
