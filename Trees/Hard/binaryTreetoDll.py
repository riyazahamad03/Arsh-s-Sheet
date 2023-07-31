class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


root = TreeNode(1)
root.left = TreeNode(3)
root.left.right = TreeNode(2)


class solution:
    def bstToDoublyLinkedList(self, root):
        head = prev = None

        def inOrder(node):
            nonlocal head, prev
            if not node:
                return None
            inOrder(node.left)

            if head == None:
                head = node
                prev = node
            else:
                node.left = head
                prev.right = node
                prev = node

            inOrder(node.right)

            return node
        return inOrder(root)


x = solution()
print(x.bstToDoublyLinkedList(root))
