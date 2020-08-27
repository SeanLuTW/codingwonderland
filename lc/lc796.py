"""
796. Rotate String


We are given two strings, A and B.

A shift on A consists of taking string A and moving the leftmost character to the rightmost position. 
For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True if and only if A can become B after some number of shifts on A.
"""

A = 'abcde'
B = 'bcdea'



if len(A) != len(B):
    print (False) 
elif B in A+A:
    print (True)

#ANS FROM DISCUSSION
#Approach 2: Simple Check 
"""
Complexity Analysis

Time Complexity: O(N^2), where N is the length of A.

Space Complexity: O(N), the space used building A+A.
"""
print( len(A) == len(B) and B in A+A)


