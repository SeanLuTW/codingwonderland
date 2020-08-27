"""
686. Repeated String Match

Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").


"""
"""
intuition:


ref:
https://leetcode.com/problems/repeated-string-match/discuss/224182/Explanation-on-the-Intuitive-Python-2-liner-solution

"""
class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
A = "abcd"
B = "cdabcdab"
from math import ceil
time = ceil(len(B)/len(A))
print (time)
for i in range(2):
    if B in (A*(time+i)):
        print (time+i)
print(-1)