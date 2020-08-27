"""
1016. Binary String With Substrings Representing 1 To N

Given a binary string S (a string consisting only of '0' and '1's) and a positive integer N, return true if and only if for every integer X from 1 to N, the binary representation of X is a substring of S.

 

Example 1:

Input: S = "0110", N = 3
Output: true
Example 2:

Input: S = "0110", N = 4
Output: false
 

Note:

1 <= S.length <= 1000
1 <= N <= 10^9
"""
"""
intuition:
idea from discussion 

TC:O(S^2)N/2 times check, O(S) to check a number in string S.The overall time complexity has upper bound O(S^2).

ref:
https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n/discuss/260847/JavaC%2B%2BPython-O(S)
"""
# class Solution:
#     def queryString(self, S: str, N: int) -> bool:
S = "0110"
N = 3
print (all(bin(i)[2:] in S for i in range(N,N//2,-1)))
print (all(bin(i)[2:] in S for i in range(N,0,-1)))#this sol works as well