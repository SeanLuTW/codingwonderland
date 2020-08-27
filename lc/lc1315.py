"""
1315. Sum of Nodes with Even-Valued Grandparent

Given a binary tree, return the sum of values of nodes with even-valued grandparent.  (A grandparent of a node is the parent of its parent, if it exists.)

If there are no nodes with an even-valued grandparent, return 0.
Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 18
Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.
"""
"""
if the node is even number we need to check if that node has grand child and add them all together 
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#idea from dis
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.sum = 0
        def dfs(node):
            if node == None:
                return None
            if node.val %2 ==0: # it's even number
                if node.left and node.left.left:
                    self.sum+=node.left.left.val#add grandson value to sum 
                if node.left and node.left.right:
                    self.sum+=node.left.right.val
                if node.right and node.right.left:
                    self.sum+=node.right.left.val
                if node.right and node.right.right:
                    self.sum+=node.right.right.val
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return self.summ