"""
445. Add Two Numbers II
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
"""

"""
intuition:
iterate two link list and start from the end of the link list
reverse two link list individually and reverse the result again
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#idea from discussion
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        linklist1 = ''
        linklist2 = ''
        #interate ll1
        while l1:
            linklist1+= str(l1.val)
            l1 = l1.next
        #iterate ll2
        while l2:
            linklist2+= str(l2.val)
            l2 = l2.next
        total = str(int(linklist1)+int(linklist2))
        dummy = ListNode(0)
        node = dummy#similiar to assign a head 
        for i in range(len(total)):
            node.next = ListNode(total[i])
            node = node.next
        return dummy.next #start from the next one instead of dummy
            