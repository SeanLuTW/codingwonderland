"""
1374. Generate a String With Characters That Have Odd Counts

Given an integer n, return a string with n characters such that each character in such string occurs an odd number of times.

The returned string must contain only lowercase English letters. If there are multiples valid strings, return any of them.  

 

Example 1:

Input: n = 4
Output: "pppz"
Explanation: "pppz" is a valid string since the character 'p' occurs three times and the character 'z' occurs once. Note that there are many other valid strings such as "ohhh" and "love".
Example 2:

Input: n = 2
Output: "xy"
Explanation: "xy" is a valid string since the characters 'x' and 'y' occur once. Note that there are many other valid strings such as "ag" and "ur".
Example 3:

Input: n = 7
Output: "holasss"
 

Constraints:

1 <= n <= 500
"""
"""
intuition:
since you can return any type of string as long as you fulfill the requirement, so I use x and y as example.
any string combine equal to n
and each string can only show up odd times
n = 4 -> xxxy or yyyx
n = 3 -> yyy or xxx
TC:O(N)
SC:O(N)
"""
class Solution:
    def generateTheString(self, n: int) -> str:
        if n %2 == 0:
            print ('x'*(n-1) + 'y')
        else:
            print ('x'*n)