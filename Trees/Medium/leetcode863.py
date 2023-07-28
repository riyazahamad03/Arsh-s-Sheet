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


class solution:
    def distanceK(self, root: TreeNode, target: int, k: int):
        q = collections.deque([(target, 0)])
        visited = set([target])
        adj = collections.defaultdict(list)

        def buildGraph(node, parent):
            if node and parent:
                adj[node.val].append(parent.val)
                adj[parent.val].append(node.val)
            if node.left:
                buildGraph(node.left, node)
            if node.right:
                buildGraph(node.right, node)
        buildGraph(root, None)
        print(adj)
        res = []
        while q:
            for _ in range(len(q)):
                node, length = q.popleft()

                if length == k:
                    res.append(node)

                for elem in adj[node]:
                    if elem not in visited:
                        visited.add(elem)
                        q.append((elem, length + 1))
        return res


x = solution()
print(x.distanceK(root, 10, 2))
