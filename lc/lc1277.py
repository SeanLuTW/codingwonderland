"""
1277. Count Square Submatrices with All Ones
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

 

Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
Example 2:

Input: matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation: 
There are 6 squares of side 1.  
There is 1 square of side 2. 
Total number of squares = 6 + 1 = 7.
"""
"""
intuition:
idea from discussion using DP 
dp[i][j] means the biggest square with matrix[i][j] as bottom-right corner.

If any matrix[i][j] == 0 meansther is no square.

If A[i][j] == 1,
we compare each corner of square dp[i-1][j-1], dp[i-1][j] and dp[i][j-1].
min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1 is the maximum size of square that we can find.
we have to remember the location  inorder to calculate square 1 or 2 or 3

"""
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:

        for i in range(1, len(A)):
            for j in range(1, len(A[0])):
                A[i][j] *= min(A[i - 1][j], A[i][j - 1], A[i - 1][j - 1]) + 1
        # print(A) #fordebug
        # print (list(map(sum, A))) #fordebug
        return( sum(map(sum, A)))