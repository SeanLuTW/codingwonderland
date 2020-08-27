"""
979. Distribute Coins in Binary Tree

Given the root of a binary tree with N nodes, each node in the tree has node.val coins, and there are N coins total.

In one move, we may choose two adjacent nodes and move one coin from one node to another.  (The move may be from parent to child, or from child to parent.)

Return the number of moves required to make every node have exactly one coin.

Example 1:



Input: [3,0,0]
Output: 2
Explanation: From the root of the tree, we move one coin to its left child, and one coin to its right child.
Example 2:



Input: [0,3,0]
Output: 3
Explanation: From the left child of the root, we move two coins to the root [taking two moves].  Then, we move one coin from the root of the tree to the right child.
Example 3:



Input: [1,0,2]
Output: 2
Example 4:



Input: [1,0,0,null,3]
Output: 4
"""
"""
intuition :
TC:O(N)where N is the number of nodes in the tree.
SC:O(H)where H is the height of the tree.

ref:
https://www.youtube.com/watch?v=zQqku1AXVF8
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.ans = 0
        self.helper(root)
        return ans
    def helper(self,root):
        if not root:
            return 0

        l = self.helper(root.left)
        r = self.helper(root.right)
        self.ans += abs(l) + abs(r)#the amount of coins that need to move is the abs value of left and right sub tree
        return l+r+root.val -1 #balance of left and balane of right and root val -1(each node require 1 coin)
