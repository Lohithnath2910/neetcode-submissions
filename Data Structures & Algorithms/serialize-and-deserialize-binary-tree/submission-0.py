# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    s = ""
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def df(r):
            if not r:
                res.append("N")
                return
            res.append(str(r.val))
            df(r.left)
            df(r.right)

        df(root)
        return ",".join(res)
    
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        m = data.split(',')
        self.i = 0

        def df():
            if m[self.i] == "N":
                self.i += 1
                return None
            no = TreeNode(int(m[self.i]))
            self.i+=1
            no.left = df()
            no.right = df()
            return no
        return df()
