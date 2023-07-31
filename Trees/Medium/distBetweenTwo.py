class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class solution:
    def pathToNode(self, root, path, k):
        if not root:
            return
        path.append(root.data)

        if root.data == k:
            return True
        if (root.left and self.pathToNode(root.left, path, k) or
                (root.right and self.pathToNode(root.right, path, k))):
            return True
        path.pop()
        return False

    def distance(self, root, data1, data2):
        if not root:
            return 0

        p1 = []
        self.pathToNode(root, p1, data1)
        p2 = []
        self.pathToNode(root, p2, data2)

        i = 0
        while i < len(p1) and i < len(p2):
            if p1[i] != p2[i]:
                break
            i += 1
        return (len(p1) + len(p2) - 2 * i)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.right = Node(7)
root.right.left = Node(6)
root.left.right = Node(5)
root.right.left.right = Node(8)

x = solution()
dist = x.distance(root, 4, 5)
print("Distance between node {} & {}: {}".format(4, 5, dist))
