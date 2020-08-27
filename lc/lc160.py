"""
160. Intersection of Two Linked Lists

Write a program to find the node at which the intersection of two singly linked lists begins.
"""
"""
intuition:
using two pointer to start with and comparing one by one
need to validate two node in a row to validate if they really joint together

Approach 3: Two Pointers
Maintain two pointers pointerA and pointerB initialized at the head of A and B, respectively. Then let them both traverse through the lists, one node at a time.
When pointerA reaches the end of a list, then redirect it to the head of B (yes, B, that's right.); similarly when pointerB reaches the end of a list, redirect it the head of A.
If at any point pointerA meets pointerB, then pointerA/pointerB is the intersection node.
To see why the above trick would work, consider the following two lists: A = {1,3,5,7,9,11} and B = {2,4,9,11}, which are intersected at node '9'.
Since B.length (=4) < A.length (=6), pointerB would reach the end of the merged list first, because pointerB traverses exactly 2 nodes less than pointerA does. By redirecting pointerB to head A, and pointerA to head B, we now ask pointerB to travel exactly 2 more nodes than pointerA would. So in the second iteration, they are guaranteed to reach the intersection node at the same time.
If two lists have intersection, then their last nodes must be the same one. So when pointerA/pointerB reaches the end of a list, record the last element of A/B respectively. If the two last elements are not the same one, then the two lists have no intersections.
"""
"""
TC:O(m+n)
SC:O(1)
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pointerA = headA#2 pointers
        pointerB = headB
        while pointerA != pointerB:
            pointerA = headB if pointerA is None else pointerA.next
            pointerB = headA if pointerB is None else pointerB.next
        return pointerA