"""
147. Insertion Sort List

Sort a linked list using insertion sort.

Algorithm of Insertion Sort:

Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
It repeats until no input elements remain.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
"""
"""
intuition:
insertion sort implement in Linklist
1. take the head node as start, compare with the next node
2.when find out the proper location, once located, connect the previous node to moved node and point to the next 
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#idea from discussion
"""
TC:O(N)
SC:O(1)
"""
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = needinsert = head

        while head and head.next:
            if head.val > head.next.val: #3->2
                #locate need to insert
                needinsert = head.next
                #locate need to insert pre
                needinsertpre = dummy
                while needinsertpre.next.val < needinsert.val:
                    needinsertpre = needinsertpre.next
                
                head.next = needinsert.next
                #connect tail and head
                #insert needtoinsert between needtoinsertpre and needtoinsertpre.nxt
                needinsert.next = needinsertpre.next
                needinsertpre.next = needinsert
            else:
                head = head.next
        return dummy.next