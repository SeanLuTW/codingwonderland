"""
1008. Construct Binary Search Tree from Preorder Traversal


Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

 

Example 1:

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

"""

"""
Intuition:
Find the left part and right part,
then recursively construct the tree.

preorder traversal root->left->right
input is a list, we have to take the first element and utlize in the tree node structure.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""
Binary search
TC:O(n^2)

"""
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:

        if not preorder:
            return None
        root = TreeNode(preorder[0])
        i = 1
        while i < len(preorder):
            if preorder[i]< preorder[0]:#calculate how many elemnt are less than root node.and it's corespond index meaning we have to place it in the left sub tree 
                 i+=1
            else:
                break
        root.left = self.bstFromPreorder(preorder[1:i])
        root.right = self.bstFromPreorder(preorder[i:])
        return root 
