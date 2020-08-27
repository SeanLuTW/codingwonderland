"""
226. Invert Binary Tree

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        #official ans recursive
        
        # if not root:
        #     return None
        # root.left, root.right = self.invertTree(root.right),self.invertTree(root.left)
        # return root
        
        #discussion idea iterative dfs
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack.extend([node.left,node.right])    
        return root
        

        #dis sol idea interative bfs
        from collections import deque
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                node.left, node.right = node.right, node.left
                queue.append(node.left)
                queue.append(node.right)
        return root
