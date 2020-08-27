"""
941. Valid Mountain Array

Given an array A of integers, return true if and only if it is a valid mountain array.

Recall that A is a mountain array if and only if:

A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]
 

Example 1:

Input: [2,1]
Output: false
Example 2:

Input: [3,5,5]
Output: false
Example 3:

Input: [0,3,2,1]
Output: true
"""

A = [0,3,2,1] 
N = len(A)
i = 0

N = len(A)
i = 0
#climb up 
while i+1 < N and A[i]< A[i+1]:
    i+=1
#peak can't be at start or end
if i==0 or i == N-1:
    print (False) 
    
#go down
while i+1 < N and A[i] > A[i+1]:
    i+=1
print (N-1 == i)