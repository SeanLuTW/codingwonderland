"""
234. Palindrome Linked List

Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
"""
"""
intuition:
reverse the first half and finding the middle at the same time
compare the reverse first half with second half
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast = slow = head 
        #find out the middle node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        #reverse the second half link list
        pre = None 
        while slow:#slow could be image as current
            next = slow.next
            slow.next = pre
            pre = slow
            slow = next
        #compare the first half with second half
        while pre:# while node and head are valid
            if pre.val != head.val:
                return False
            pre = pre.next
            head = head.next
        return True