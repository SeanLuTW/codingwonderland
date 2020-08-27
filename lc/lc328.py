"""
328. Odd Even Linked List

Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
"""
"""
intuition:
create two empty list and iterate original link list append each node one by one for each list
after hit null combine two list together
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#idea from discussion
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        odd = ListNode(0)#initialize odd link list with starting value 0
        even = ListNode(0)#initialize even link list with starting value 0
        odd_head = odd #inital head of odd link list 
        even_head =even#initial head of even link list
        isodd = True
        while head:
            if isodd:
                odd.next = head #original head give it to odd link list
                odd = odd.next
            else:
                even.next = head#original head give it to even link list
                even = even.next
            isodd = not isodd #switch to the other link list
            head = head.next #move on to the next node in the original link list
        even.next = None #address null at the end of the even link list
        odd.next = even_head.next #combine two link list together 
        return odd_head.next