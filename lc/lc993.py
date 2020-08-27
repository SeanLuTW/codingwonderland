"""
993. Cousins in Binary Tree

In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        #remember the parent and depth
        parent = {}
        depth = {}
        def dfs(node, par = None):
            if node:
                depth[node.val] = 1 + depth[par.val] if par else 0
                parent[node.val] = par
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)
        return depth[x] == depth[y] and parent[x] != parent[y]  

        #self trying 
        parent = {}
        depth = {}
        def dfs(node,mom = None):
            if node is not None:
                if mom is not None:
                    depth[node.val] = 1 + depth[mom.val]
                else:
                    depth[node.val] = 0
                
                parent[node.val] = mom
                dfs(node.left,node)
                dfs(node.right,node)

        dfs(root)
        return depth[x] == depth[y] and parent[x] != parent[y]