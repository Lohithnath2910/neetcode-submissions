# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.c = 0
        return self.d(root) != -1
       

    def d(self,n):
        if not n:
            return 0
        
        l = self.d(n.left)
        if l == -1:
            return -1
        r = self.d(n.right)
        if r == -1:
            return -1

        if abs(l-r) > 1:
            return -1
        

        return 1 + max(l,r)
        