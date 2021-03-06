"""
572. Subtree of Another Tree

Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
"""
"""
intuition:
using dfs, For each node of s, let's check if it's subtree equals t.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    #convert the BT to string start node with "^" if it's the end of node add "N" as remark
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def convert(p):
            return( "^" + str(p.val) + "#" + convert(p.left) + convert(p.right) if p else "N")

        return convert(t) in convert(s)

