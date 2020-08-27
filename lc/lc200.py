"""
200. Number of Islands

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""
"""
intuition:
DFS

TC:O(mn)
SC:O(mn)
ref:
http://zxi.mytechroad.com/blog/searching/leetcode-200-number-of-islands/
https://leetcode.com/problems/number-of-islands/discuss/56340/Python-Simple-DFS-Solution
"""

class Solution:
    def numIslands(self, grid):
        row = len(grid)
        col = len(grid[0])
        if not row:
            return 0
        ans = 0
        for i in range(row):
            for j in range (col):
                if grid[i][j]=='1':
                    self.dfs(grid,i,j)
                    ans+=1
        return ans
    def dfs(self,grid,i,j,row,col):
        if i<0 or j<0 or i>=row or j >=col or grid[i][j]=='0':
            return 
        grid[i][j]='0'
        self.dfs(grid,i+1,j)
        self.dfs(grid,i-1,j)
        self.dfs(grid,i,j+1)
        self.dfs(grid,i,j-1)


