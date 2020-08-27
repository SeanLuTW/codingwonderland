"""
669. Trim a Binary Search Tree


Given a binary search tree and the lowest and highest boundaries as L and R,
trim the tree so that all its elements lies in [L, R] (R >= L).
You might need to change the root of the tree, so the result should return the new root of the trimmed binary search tree.


"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        #dis sol
        if not root:
            return None
        if root.val < L:
            return self.trimBST(root.right,L,R)
        elif root.val>R:
            return self.trimBST(root.left,L,R)
        root.left = self.trimBST(root.left,L,R)
        root.right = self.trimBST(root.right,L,R)
        return root
        
        #official sol 1
        # def trim(node):
        #     if not node:
        #         return None
        #     elif node.val < L:
        #         return trim(node.right)
        #     elif node.val> R:
        #         return trim(node.left)
        #     else:#kepp looking for node in range
        #         node.left = trim(node.left)
        #         node.right = trim(node.right)
        #         return node

        # return trim(root)