# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        co = 0
        return self.s(root,co)
    
    def s(self,r,c):
        if not r:
            return c
        
        c = max(self.s(r.left,c)+1,self.s(r.right,c)+1)
        return c
        