class TreeNode:
    def __init__(self, val=0, left=None, right=None, next=None) -> None:
        self.val = val
        self.left = left
        self.right = right
        self.next = next


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(12)


class solution:
    def connect(self, node: TreeNode):
        curr, nxt = node, node.left if node else None
        while curr and nxt:
            curr.left.next = curr.right

            if curr.next:
                curr.left.next = curr.next.left

            curr = curr.next
            if curr:
                curr = nxt
                nxt = curr.left
        return node


x = solution()
print(x.connect(root))
