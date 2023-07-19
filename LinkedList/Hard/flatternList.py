class Node():
    def __init__(self, data):
        self.data = data
        self.right = None
        self.down = None


class LinkedList():
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.down = self.head
        self.head = new_node


class solution:
    def merge(self, a, b):
        dummy = Node(0)
        curr = dummy
        while a and b:
            if a.data < b.data:
                curr.down = a
                curr = curr.down
                a = a.down
            else:
                curr.down = b
                curr = curr.down
                b = b.down
        if a:
            curr.down = a
        elif b:
            curr.down = b

        return dummy.down

    def flatten(self, root):
        if root is None or root.right is None:
            return root

        root.right = self.flatten(root.right)

        root = self.merge(root, root.right)
        return root


L = LinkedList()

'''
    Let us create the following linked list
            5 -> 10 -> 19 -> 28
            |    |     |     |
            V    V     V     V
            7    20    22    35
            |          |     |
            V          V     V
            8          50    40
            |                |
            V                V
            30               45
    '''
L.push(30)
L.push(8)
L.push(7)
L.push(5)

L.head.right = Node(10)
L.head.right.down = Node(20)

L.head.right.right = Node(19)
L.head.right.right.down = Node(22)

L.head.right.right.right = Node(28)
L.head.right.right.right.down = Node(35)
L.head.right.right.right.down.down = Node(40)
L.head.right.right.right.down.down.down = Node(45)

x = solution()
result = x.flatten(L.head)

# Printing the flattened linked list
while result:
    print(result.data, end=" -> ")
    result = result.down
