"""
235. Lowest Common Ancestor of a Binary Search Tree

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]

Example 1:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
find out two nodes that has the colsest same root
Algorithm

Start traversing the tree from the root node.
If both the nodes p and q are in the right subtree, then continue the search with right subtree starting step 1.
If both the nodes p and q are in the left subtree, then continue the search with left subtree starting step 1.
If both step 2 and step 3 are not true, this means we have found the node which is common to node p's and q's subtrees. and hence we return this common node as the LCA.
"""
#idea from solution
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parentval = root.val
        pval = p.val
        qval = q.val
        #both p and q are larger than parent
        if p.val > parentval and q.val > parentval:
            return self.lowestCommonAncestor(root.right, p, q)
        #both p and q are less then parent
        elif p.val < parentval and q.val < parentval:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root


"""
TC:O(N) where N is the number of nodes in the BST.
In the worst case we might be visiting all the nodes of the BST.
SC:O(N) his is because the maximum amount of space utilized by the recursion stack would be N since the height of a skewed BST could be N.
"""