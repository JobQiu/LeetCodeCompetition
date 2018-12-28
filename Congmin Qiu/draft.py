class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None

        i = 1
        j = 0
        root = TreeNode(preorder[0])
        s = [root]
        n = len(preorder)
        while i < n:
            # check if top has more left nodes
            if inorder[j] != s[-1].val:
                node = TreeNode(preorder[i])
                s[-1].left = node
                s.append(node)
                i += 1
            else:
                # while s and preorder[i] != inorder[j]:
                while s and s[-1].val == inorder[j]:
                    parent = s.pop()
                    j += 1

                node = TreeNode(preorder[i])
                parent.right = node
                s.append(node)
                i += 1

        return root


s = Solution()
res = s.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
print(res)
