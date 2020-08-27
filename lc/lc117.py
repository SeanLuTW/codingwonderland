"""
117. Populating Next Right Pointers in Each Node II

Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 

Follow up:

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.
 

Example 1:



Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
 

Constraints:

The number of nodes in the given tree is less than 6000.
-100 <= node.val <= 100
"""
""""""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
""""""
from queue import Queue
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return 
        que = [root]
        while que:
            cur = que.pop(0)
            if cur.left and cur.right:
                cur.left.next = cur.right
                if cur.next:
                    if cur.next.left:
                        cur.right.next = cur.next.left
                    else:
                        cur.right.next = cur.next.right
                que.append(cur.left)
                que.append(cur.right)
        return root

    def connect(self,root):
        if not root:
            return 
        que = [root]
        level = []
        while que:
            cur = que.pop(0)
            if cur.left:
                level.append(cur.left)
            if cur.right:
                level.append(cur.right)
            if que:
                cur.next = que[0]
            else:
                None
            if not que and level:
                que = level
                level = que
