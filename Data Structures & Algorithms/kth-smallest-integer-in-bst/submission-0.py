# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    c = 0
    f = 0
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.d(root,k)
        

    def d(self,root,k):
        if root == None:
            return None

        self.d(root.left,k)
        self.c += 1
        if(self.c == k):
            self.f = root.val
        self.d(root.right,k)
        return self.f
        