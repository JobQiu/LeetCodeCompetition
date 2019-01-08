class Solution:
    def delEdge(self, root ):
        def dfs(root, min_, max_ ):
            if root == None or root.val <= min_ or root.val >= max_val:
                return None
            root.left = dfs(root.left, min_, root.val)
            root.right= dfs(root.right,root.val, max_)
            return root
        return dfs(root, float("-inf"), flost("inf"))


class TreeNode:
    val
    left = None
    right = None

    def __init__(self, val ):
        self.val = val

    def printTree(self ):
        
        pass
