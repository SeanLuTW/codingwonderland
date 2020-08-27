"""
671. Second Minimum Node In a Binary Tree


Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes. More formally, the property root.val = min(root.left.val, root.right.val) always holds.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

Example 1:

Input: 
    2
   / \
  2   5
     / \
    5   7

Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.
 

Example 2:

Input: 
    2
   / \
  2   2

Output: -1
Explanation: The smallest value is 2, but there isn't any second smallest value.
"""
"""
intuition:
initialize a variable 
put root.val into that variable 
iterate all the node in the tree
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""
TC:O(N)
SC:O(N)
Time Complexity: O(N), where N is the total number of nodes in the given tree. We visit each node exactly once, and scan through the O(N)O(N) values in unique once.

Space Complexity: O(N), the information stored in uniques.
"""
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        nodesset = set()
        def dfs(node):
            if node:
                nodesset.add(node.val)
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        minium = min(nodesset)
        ans = float('inf')
        for i in nodesset:
            if minium < i<ans:
                ans = i
            
        return ans if ans< float('inf') else -1