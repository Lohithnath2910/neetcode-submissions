# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        k = deque()
        k.append(root)

        while k:
            ad = []
            for i in range(len(k)):
                n = k.popleft()
                n1 = n.val
                ad.append(n1)
                if n.left:
                    k.append(n.left)
                if n.right:
                    k.append(n.right)
            ans.append(ad)
        return ans


        

