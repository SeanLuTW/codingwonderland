"""
1380. Lucky Numbers in a Matrix

Given a m * n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

 

Example 1:

Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column
Example 2:

Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
Output: [12]
Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.
Example 3:

Input: matrix = [[7,8],[1,2]]
Output: [7]
"""
"""
Intuition: [idea from discussion]
using set as contatiner
iterate each list in list find out min in each list 
reverse the matrix using zip(*) 

Analysis:
TC:O(m*n)
SC:(m+n)
"""
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        minrow = {min(r) for r in matrix}#using set as data type 
        maxcol = {max(c)for c in zip(*matrix)}#zip(*)
        # print (minrow & maxcol)# and operator to find the intersection
        return (list(minrow & maxcol))#return as list type