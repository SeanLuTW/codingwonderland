"""
938. Range Sum of BST

Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.

 

Example 1:

Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32
Example 2:

Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        ans = 0 
        if not root:
            return 0        
        if L <= root.val <= R:
            ans += root.val   
        if root.val < L:
            # Case when left subtree has values < L so need to traverse it
            ans+=self.rangeSumBST(root.right,L,R)
        elif root.val > R:
            # Case when right subtree has values > R so need to traverse it
            ans+=self.rangeSumBST(root.left,L,R)
        else:
            # Case when both subtrees shall be traversed
            ans+=self.rangeSumBST(root.left,L,R)+self.rangeSumBST(root.right,L,R)
        return ans