"""
538. Convert BST to Greater Tree

Given a Binary Search Tree (BST), convert it to a Greater Tree
such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13
"""
"""
#start from right and remember it's value add it to the next node
#RVL
#start recursive from right, then visiteing node, then left 
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
recursive solution 
TC:O(n)
SC:O(n)
Complexity Analysis

Time complexity : O(n)

A binary tree has no cycles by definition, so convertBST gets called on each node no more than once.
Other than the recursive calls, convertBST does a constant amount of work, so a linear number of calls to convertBST will run in linear time.

Space complexity : O(n)

Using the prior assertion that convertBST is called a linear number of times, we can also show that the entire algorithm has linear space complexity. 
Consider the worst case, a tree with only right (or only left) subtrees. The call stack will grow until the end of the longest path is reached, which in this case includes all nn nodes.
"""
class Solution(object):
    def __init__(self):
        self.total = 0
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        if root is not None:
            self.convertBST(root.right)
            self.total += root.val
            root.val = self.total
            self.convertBST(root.left)
        return root