# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.m = float("-inf")

        def df(r):
            if r == None:
                return 0
            
            lb = max(0,df(r.left))
            rb = max(0,df(r.right))

            curr = r.val + lb + rb

            self.m = max(self.m,curr)

            return r.val + max(lb,rb)

        df(root)
        return self.m
