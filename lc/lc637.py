"""
637. Average of nodevalues in Binary Tree

Given a non-empty binary tree, return the average nodevalue of the nodes on each nodevalue in the form of an array.

Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average nodevalue of nodes on nodevalue 0 is 3,
on nodevalue 1 is 14.5,
and on nodevalue 2 is 11. Hence return [3, 14.5, 11].
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfnodevalues(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        # ans = [root.val]
        # parents = [root]
        # children = []
        # nodevalue = []
        # while True :
        #     for i in parents:
        #         if i.left not None:
        #             nodevalue.append(i.left.val)
        #             children.append(i.left)
        #         if i.right not None:
        #             nodevalue.append(i.right.val)
        #             children.append(i.right)
        #     if len(nodevalue)>0:
        #         ave = float(sum(nodevalue)/len(nodevalue)) 
        #         ans.append(ave)
        #         parents = list(children)
        #         children = []
        #         nodevalue = []
        #     else:
        #         break
        # return ans 

        #seltrying
        # ans = [root.val]
        # parent = [root]
        # children = []
        # nodevalue = []
        # while True:
        #     for i in parent:
        #         if i.left != None:
        #             children.append(i.left)
        #             nodevalue.append(i.left.val)
        #         if i.right!= None:
        #             children.append(i.right)
        #             nodevalue.append(i.right.val)
        #     if len(nodevalue) >0:
        #         ave = float(sum(nodevalue))/len(nodevalue)
        #         ans.append(ave)
        #         parent = list(children)
        #         children = []
        #         nodevalue = []
        #     else:
        #         break
        # return ans 


        #dis ans
        arr=[]
        level=[root]
        while(level):
            s=0
            st=[]
            for a in level:
                s=s+a.val
                if(a.left):
                    st.append(a.left)
                if(a.right):
                    st.append(a.right)
            arr.append(float(s)/len(level))
            level=st
        return arr







