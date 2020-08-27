"""
242. Valid Anagram
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""

s= "anagram"
t = "nagaram"
from collections import Counter 
"""
TC:O(nlogn)
SC:O(1)
"""
print (sorted(s))
print (sorted(t))
print (sorted(s) == sorted(t))
cnts = Counter(s)
cntt = Counter(t)

#idealy the total count for each string should be the same
# print(cnts)#fd
# print (cntt)#fd
cnts.subtract(cntt)
print (sum(list(cnts[i] for i in cnts))==0)
