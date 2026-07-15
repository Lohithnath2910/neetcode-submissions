# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    c = 0
    def goodNodes(self, root: TreeNode) -> int:
        if root == None:
            return 0
        self.d(root,-101)
        return self.c

    def d(self,r,an):
        if not r:
            return None
        
        if r.val > an:
            an = r.val
        
        if r.val >= an:
            self.c += 1

        self.d(r.left,an)
        self.d(r.right,an)

