# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        f = self.s(root,subRoot)
        return self.k(f,subRoot)

    def s(self,r,sr):
        if(r == None):
            return None
        
        if(r.val == sr.val and self.k(r, sr)):
            return r
        
        left = self.s(r.left,sr)
        if left:
            return left

        return self.s(r.right,sr)
    
    def k(self,r,sr):
        if(r == None and sr == None):
            return True
        
        if(r == None or sr == None):
            return False
        
        if(r.val != sr.val):
            return False

        return self.k(r.left,sr.left) and self.k(r.right,sr.right)
        


        