"""
701. Insert into a Binary Search Tree


Given the root node of a binary search tree (BST) and a value to be inserted into the tree, insert the value into the BST. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Note that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

For example, 

Given the tree:
        4
       / \
      2   7
     / \
    1   3
And the value to insert: 5
You can return this binary search tree:

         4
       /   \
      2     7
     / \   /
    1   3 5
This tree is also valid:

         5
       /   \
      2     7
     / \   
    1   3
         \
          4


"""

"""
idea:
dfs
first we will check each node in the tree start from the root node value, since it's BST so if the val is smaller than root val we go left, if it's larger we go right.
TC:O(n)
SC:O(n)
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""
Recursive 
"""
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        if root.val> val:
            root.left = self.insertIntoBST(root.left,val)
        else :
            root.right = self.insertIntoBST(root.right,val)

        return root 

"""
Iterative
"""

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        current = root 
        parent = None
        #similiar to dfs goes all the way down 
        while current is not None:
            # we go left 
            if val < current.val:
                parent = current
                current = current.left
            #we go right
            else:
                parent = current
                current = current.right
        if val < parent.val:
            parent.left = TreeNode(val)
        else:
            parent.right = TreeNode(val)

        return root 
