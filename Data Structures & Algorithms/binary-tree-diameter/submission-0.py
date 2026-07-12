# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        c = self.d(root)
        return self.res
    
    def d(self,n):
        if not n:
            return 0
        
        l = self.d(n.left)
        r = self.d(n.right)

        self.res = max(self.res,l + r)

        return 1 + max(l,r)