

import collections

class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


root = TreeNode(10)
root.left = TreeNode(2)
root.right = TreeNode(11)
root.left.left = TreeNode(1)
root.left.right = TreeNode(5)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(6)
root.left.right.left.right = TreeNode(4)

class Solution:
    def verticalTraversal(self, root: TreeNode):
        if not root:
            return []

        q = collections.deque()
        q.append((root, 0))  # (node, horizontal distance)
        vMap = collections.defaultdict(list) 

        while q:
            level_size = len(q)
            temp_map = collections.defaultdict(list)

            for _ in range(level_size):
                node, horizontal = q.popleft()
                temp_map[horizontal].append(node.val)

                if node.left:
                    q.append((node.left, horizontal - 1))

                if node.right:
                    q.append((node.right, horizontal + 1))

            for horizontal, nodes in temp_map.items():
                vMap[horizontal].extend(sorted(nodes))
        vertical_order = [vMap[horizontal] for horizontal in sorted(vMap)]

        return vertical_order