"""
1314. Matrix Block Sum

Given a m * n matrix mat and an integer K, return a matrix answer where each answer[i][j] is the sum of all elements mat[r][c] for i - K <= r <= i + K, j - K <= c <= j + K, and (r, c) is a valid position in the matrix.
 

Example 1:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], K = 1
Output: [[12,21,16],[27,45,33],[24,39,28]]
Example 2:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], K = 2
Output: [[45,45,45],[45,45,45],[45,45,45]]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n, K <= 100
1 <= mat[i][j] <= 100
"""
"""
TC:O(m*n)
SCO(m*n)
"""
mat = [[1,2,3],[4,5,6],[7,8,9]]
K = 2
row = len(mat)
col = len(mat[0])
#build up dp array
dp = [[0 for _ in range (col+1)] for _ in range(row+1)]
#iterate dp table 
for i in range (1,row+1):
    for j in range (1,col+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]-dp[i-1][j-1] + mat[i-1][j-1]
# print (dp)
ans = [[0] * col for _ in range(row)]
for i in range(row):
    for j in range(col):
        r1 = max(0,i-K)
        c1 = max(0,j-K)
        r2 = min (row,i+K+1)#+1 maybe it's help to avoid index out of bound error
        c2 = min(col,j+K+1)#+1 maybe it's help to avoid index out of bound error
        ans[i][j] = dp[r2][c2]-dp[r1][c2]-dp[r2][c1]+dp[r1][c1]

print (ans)