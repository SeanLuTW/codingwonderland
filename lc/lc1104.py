"""
1104. Path In Zigzag Labelled Binary Tree


In an infinite binary tree where every node has two children, the nodes are labelled in row order.

In the odd numbered rows (ie., the first, third, fifth,...), the labelling is left to right, while in the even numbered rows (second, fourth, sixth,...), the labelling is right to left.


Given the label of a node in this tree, return the labels in the path from the root of the tree to the node with that label.

 

Example 1:

Input: label = 14
Output: [1,3,4,14]
Example 2:

Input: label = 26
Output: [1,2,6,10,26]
 

Constraints:

1 <= label <= 10^6
"""
"""
intuition:
no logic way to solve this problem
it's kind of a math problem.
this question is talk about a tree will have a seq number following by "Z" shape
the label node will be provided you have to find out the path from root to the label node

example:
label=14, label / 2 = 7, 7 XOR 3(0b11) = 4
4 / 2 = 2, 2 XOR 1(0b1) = 3
3 / 2 = 1, 1 XOR 0(0b0) = 1
"""
#idea from discussion 
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        #convert label to binary 
        #get the length of the label - 4 
        #apply by power of 2 
        #minus 1
        #XOR with label //2
        return (self.pathInZigZagTree(label//2 ^ 2**(len(bin(label))-4)-1) if label > 1 else []) + [label]
