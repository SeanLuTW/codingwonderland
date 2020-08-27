"""
429. N-ary Tree Level Order Traversal

Given an n-ary tree,
return the level order traversal of its nodes' values. (ie, from left to right, level by level).
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """

        #dis sol1 iterative 
        # if not root:
        #     return []
        # ans = []
        # queue= [root]
        # while queue:
        #     tmp = []
        #     childlist = []
        #     for node in queue:
        #         tmp.append(node.val)
        #         for child in node.children:
        #             childlist.append(child)

        #     queue = childlist
        #     ans.append(tmp)
        # return ans

        ans = []
        if not root:
            return []
        queue = [root]
        while any(queue):
            ans.append([node.val for node in queue])
            queue = [child for node in queue for child in node.children]
        return ans