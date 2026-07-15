# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        k = deque()
        ans = []
        aa = []
        k.append(root)

        while k:
            aa = []
            for i in range(len(k)):
                n = k.popleft()
                n1 = n.val
                aa.append(n1)
                if n.left:
                    k.append(n.left)
                if n.right:
                    k.append(n.right)
            ans.append(self.c(aa))

        return ans
    
    def c(self,a):
        return a[len(a)-1]
