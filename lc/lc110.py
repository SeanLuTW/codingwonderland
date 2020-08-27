"""
110. Balanced Binary Tree

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
"""

"""
intuition:
since the requirement is each node in tree the diff has to less than the height of the tree,
so 

An empty tree is height-balanced. A non-empty binary tree T is balanced if:
1) Left subtree of T is balanced
2) Right subtree of T is balanced
3) The difference between heights of left subtree and right subtree is not more than 1.
"""
"""
TC:O(n^2)
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def checkheight(self,root):
        if not root:
            return 0

        return 1+ max(self.checkheight(root.left),self.checkheight(root.right))
    
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True #this is a tricky case if there is nothing in the tree still count as balanced 
        return abs(self.checkheight(root.left)-self.checkheight(root.right))<=1 and self.isBalanced(root.left) and self.isBalanced(root.right)

