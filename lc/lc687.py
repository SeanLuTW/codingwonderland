"""
687. Longest Univalue Path


Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

The length of path between two nodes is represented by the number of edges between them.

 

Example 1:

Input:

              5
             / \
            4   5
           / \   \
          1   1   5
Output: 2

 

Example 2:

Input:

              1
             / \
            4   5
           / \   \
          4   4   5
Output: 2

 

Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.
"""
#idea from discussion
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""
TC:O(N)
SC:O(N)
"""
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.longestpath = 0
        def traversal(node,parent_value):
            if not node:
                return 0 
            left,right = traversal(node.left,node), traversal(node.right,node)
            self.longestpath = max(self.longestpath,left+right)
            return 1 + max(left,right) if node.val == parent_value else 0
        traversal(root,None)
        return self.longestpath

"""
TC:O(N)
SC:O(N)
"""
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.longest = 0
        def traverse(node):
            if not node:
                return 0 
            left_length, right_length = traverse(node.left), traverse(node.right)
            left = (left_length+1) if node.left and node.left.val == node.val else 0
            right = (right_length+1) if node.right and node.right.val == node.val else 0 
            self.longest = max(self.longest,left+right)
            return max (left,right)
        traverse(root)
        return self.longest