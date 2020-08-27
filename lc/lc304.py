"""
304. Range Sum Query 2D - Immutable

Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12
Note:
You may assume that the matrix does not change.
There are many calls to sumRegion function.
You may assume that row1 ≤ row2 and col1 ≤ col2.
"""
"""
intuition:
TC:O(1) time per query, O(mn) time for pre-computation 
SC:O(mn)

ref:
https://leetcode.com/problems/range-sum-query-2d-immutable/discuss/75448/Sharing-My-Python-solution
"""
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        #edge case
        if matrix is None or not matrix:
            return
        row = len(matrix)
        col = len(matrix[0])
        #build up 2D array
        self.dp = [[0 for _ in range(col+1)]for _ in range(row+1)]
        #start pre-computing
        for i in range(1,row+1):
            for j in range(1,col+1):
                self.dp[i][j] = self.dp[i-1][j]+self.dp[i][j-1]-self.dp[i-1][j-1]+matrix[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        #ABCD = OD-OC-OB+OA
        row1 = row1+1
        col1 = col1+1
        row2 = row2+1
        col2 = col2+1
        
        return self.dp[row2][col2] - self.dp[row2][col1-1]-self.dp[row1-1][col2] +self.dp[row1-1][col1-1]