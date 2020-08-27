"""
1028. Recover a Tree From Preorder Traversal

We run a preorder depth first search on the root of a binary tree.

At each node in this traversal, we output D dashes (where D is the depth of this node), then we output the value of this node.  (If the depth of a node is D, the depth of its immediate child is D+1.  The depth of the root node is 0.)

If a node has only one child, that child is guaranteed to be the left child.

Given the output S of this traversal, recover the tree and return its root.
Example 1:
Input: "1-2--3--4-5--6--7"
Output: [1,2,5,3,4,6,7]

Example 2:
Input: "1-2--3---4-5--6---7"
Output: [1,2,5,3,null,6,null,4,null,7]
 

Example 3:

Input: "1-401--349---90--88"
Output: [1,401,null,349,88,90]
"""
"""
intuition:

pre-order traversal :root->left->right

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#idea from discussion
class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        import re
        charandvalue = [(len(s[0]),int(s[1])) for s in re.findall("(-*)(\d+)",S)][::-1]

        def construct(level):
            if not charandvalue or level!= charandvalue[-1][0]:return None
            node = TreeNode(charandvalue.pop()[1])# IN INDEX 1 IT'S INTERGER, starting poping from the last node in the list
            node.left = construct(level+1)
            node.right = construct(level+1)
            return node
        return (construct(0))