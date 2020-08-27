"""
437. Path Sum III

You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11

"""
"""
DFS problem
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
ref disscussion
Brute Froce Sol:
traverse each node (preorder traverse) and find out all the path which sum to target using this node as root.
"""
class Solution:
    def findpath(self,root,target):
        if root:
            return int(root.val == target) + self.findpath(root.left, target-root.val) + self.findpath(root.right, target-root.val)
        return 0 
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if root:
            return self.findpath(root,sum) + self.findpath(root.left,sum) + self.findpath(root.right,sum)
        return 0 

"""
B.F. 2
count total sol
count current remain value
SC:O(1)due to there is no extra cache. However, for any recursive question, we need to think about stack overflow, namely the recursion should not go too deep.
TC:O(n^2)
Time complexity depends on the two DFS.
1st layer DFS will always take O(n), due to here we will take each node out, there are in total n TreeNodes
2nd layer DFS will take range from O(n) (single sided tree) to O(logn)(balanced tree). This is due to here we are get all the paths from a given node. The length of path is proportional to the tree height.
Therefore, the total time complexity is O(nlogn) to O(n^2).
"""
class Solution:
    def test(self,node,target):
        if node is None:
            return 
        if node.val == target:
            self.totalpath +=1
        self.test(node.left, target-node.val)
        self.test(node.right, target-node.val)
    #define a dfs function to traverse through the tree, at each tree node, call another DFS to test of the path sum include answer
    def dfs(self,node,target):
        if node is None:
            return
        #start dfs in any order, i use preorder here
        self.test(node, target)
        self.dfs(node.left, target)
        self.dfs(node.right,target)

    def pathSum(self, root: TreeNode, sum: int) -> int:
        #define a var to save total path
        self.totalpath = 0
        # 1st layer DFS to go through each node
        self.dfs(root,sum)
        return self.totalpath
"""
Memoize solution 
"""
from collections import defaultdict
class Solution:
    def pathSum(self, root, target):
        self.ans = 0
        cache = defaultdict(int)
        cache[0] = 1
        
        def dfs(root, cur_sum):
            if not root:
                return 
            cur_sum += root.val
            self.ans += cache[cur_sum - target]
            cache[cur_sum] += 1
            dfs(root.left, cur_sum)
            dfs(root.right, cur_sum)
            cache[cur_sum] -= 1
            
        dfs(root, 0)
        return self.ans