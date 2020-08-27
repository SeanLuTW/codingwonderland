"""
1260. Shift 2D Grid

Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.

In one shift operation:

Element at grid[i][j] moves to grid[i][j + 1].
Element at grid[i][n - 1] moves to grid[i + 1][0].
Element at grid[m - 1][n - 1] moves to grid[0][0].
Return the 2D grid after applying shift operation k times.

 

Example 1:
Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[9,1,2],[3,4,5],[6,7,8]]
"""
"""
intuition:
TC:O(n*m*k)
SC:O(1)If the input and output are the same type.We aren't creating any new data structures.
"""
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        row = len(grid)
        col = len(grid[0])
        for _ in range(k):
            last = grid[-1][-1]#take out the last element in the grid 
            for i in range(row):
                for j in range(col):
                    tmp = grid[i][j]#put the first handle cell in tmp
                    grid[i][j] = last#give last cell to first cell
                    last = tmp #original first element to last 
        return grid