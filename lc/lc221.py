"""
221. Maximal Square

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4

"""
#PT:DP
"""
intuition:
clear dp question
TC:O(m*n)
SC:O(m*n)

ref:
https://leetcode.com/problems/maximal-square/discuss/600149/Python-Thinking-Process-Diagrams-DP-Approach
"""
# class Solution:
#     def maximalSquare(self, matrix: List[List[str]]) -> int:

matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
if matrix is None or len(matrix) < 1:
    print (0)
row = len(matrix)
column = len(matrix[0])
#create dp table
dp = [[0 for _ in range(column+1)] for _ in range(row+1)]
# dp = [[0]*(column+1) for _ in range(row+1)]
# print (dp)
sidemax = 0
#start handling dp table
for i in range (row):
    for j in range (column):
        if matrix[i][j] == '1':
            dp[i+1][j+1] = min(dp[i][j],dp[i+1][j],dp[i][j+1])+1
            sidemax = max(sidemax,dp[i+1][j+1])

print (sidemax**2)