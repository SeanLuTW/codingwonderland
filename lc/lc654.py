"""
654. Maximum Binary Tree

Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this tree.

Example 1:
Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    / 
     2  0   
       \
        1
"""
"""
# Not clear  abt the question, so I leverage the solution description
1.we have to find out the largest num in the array and set it as root also save the index of that number(root) 
2.start from the root we split into two sub array one is left and the other one is right
3.we construct the tree node using recurtion method

TC:O(n^2)
SC:O(n)
"""
"""
T(n) = T(n-1) {Left Sub} + T(1) {Right Sub} + O(n) {find out max} + O(1) {To connect left and right tree}
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        
        rootval = max(nums)
        rootindex = nums.index(rootval) 

        root = TreeNode(rootval)
        root.left = self.constructMaximumBinaryTree(nums[0:rootindex])
        root.right = self.constructMaximumBinaryTree(nums[rootindex+1:len(nums)])
    
        return root