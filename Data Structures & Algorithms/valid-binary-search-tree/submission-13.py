# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.d(root,float("-inf"),float("inf"))
    
    def d(self,r,li,re):
        if not r:
            return True

        if not (li < r.val < re):
            return False

        return self.d(r.left,li,r.val) and self.d(r.right,r.val,re)


        