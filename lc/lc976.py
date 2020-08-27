"""
976. Largest Perimeter Triangle
Given an array A of positive lengths, return the largest perimeter of a triangle with non-zero area, formed from 3 of these lengths.

If it is impossible to form any triangle of non-zero area, return 0.

Example 1:

Input: [2,1,2]
Output: 5
Example 2:

Input: [1,2,1]
Output: 0
Example 3:

Input: [3,2,3,4]
Output: 10
Example 4:

Input: [3,6,2,3]
Output: 8
"""

A = [2,1,2]
"""
For a >= b >= c, a,b,c can form a triangle if a < b + c.
any two length sum should be greater than the rest of the length
sort the array first and reverse it, place the bigger number in the front
If A[n-1] < A[n-2] + A[n-3], we will get a triangle
"""
class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        #idea from discusstion 
        A = sorted(A)[::-1]
        for i in range(len(A) - 2):
            if A[i] < A[i + 1] + A[i + 2]:
                return( A[i] + A[i + 1] + A[i + 2])
        return 0
