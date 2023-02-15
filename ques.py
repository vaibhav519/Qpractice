class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        
        stack = [root]

        while stack:
            root = stack.pop()
            if root.val == p.val: return root.val
            if root.val == q.val: return root.val
            if p.val < root.val < q.val: return root.val

            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)


root = TreeNode(6)
root.left = TreeNode(2)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)
root.right = TreeNode(8)
root.right.right = TreeNode(9)
root.right.left = TreeNode(7)
obj = Solution()
print(obj.lowestCommonAncestor(root, root.left.left, root.left.right))
