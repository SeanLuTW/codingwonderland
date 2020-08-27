"""
1022. Sum of Root To Leaf Binary Numbers

Given a binary tree, each node has value 0 or 1.  Each root-to-leaf path represents a binary number starting with the most significant bit.  For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.

For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.

Return the sum of these numbers.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        """
        TC:O(n)
        SC:O(n)
        """
        #find out if there node has child 
        def dfs(node, path=None):
            if path == None:
                path = ''
            if node:
                path += str(node.val)
                if node.left or node.right:
                    return dfs(node.left, path) + dfs(node.right, path)
                else:
                    return int(path, 2)
            else:
                return 0
        # return sumRootToLeaf(root)
root = TreeNode([1,0,1,0,1,0,1])
a = Solution()
a.sumRootToLeaf(root)
