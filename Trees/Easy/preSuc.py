class TreeNode:
    def __init__(self, key) -> None:
        self.key = key
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
    def findPreSuc(self, root, pre, suc, key):
        node1, node2 = root, root
        while node1:
            if node1.key >= key:
                node1 = node1.left
            else:
                pre = node1
                node1 = node1.right
        while node2:
            if node2.key <= key:
                node2 = node2.right
            else:
                suc = node2
                node2 = node2.left
        return pre , suc

pre , suc = TreeNode(None) , TreeNode(None)
x = Solution()
pre , suc  = x.findPreSuc(root, pre , suc , 8)
if pre != None:
    print(pre.key)

if suc != None:
    print(suc.key)