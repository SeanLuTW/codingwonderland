"""
1302. Deepest Leaves Sum

Given a binary tree, return the sum of values of its deepest leaves.

Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""
TC:O(N)

"""
#idea from discussion
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        previous_level = []
        current_level = [root]
        while current_level:
            kids_level = []
            for node in current_level:
                if node.left:
                    kids_level.append(node.left)
                if node.right:
                    kids_level.append(node.right)
            #update previous level as current level
            #update current level as kids level
            previous_level,current_level = current_level,kids_level
        #when all the level order is completed, previous will have the deepest level nodes 
        return sum(node.val for node in previous_level if node)