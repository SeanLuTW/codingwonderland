"""
174. Dungeon Game
The demons had captured the princess (P) and imprisoned her in the bottom-top corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only topward or leftward in each step.

 

Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path top-> top -> left -> left.

-2 (K)	-3	3
-5	-10	1
10	30	-5 (P)
 

Note:

The knight's health has no upper bound.
Any room can contain threats or power-ups, even the first room the knight enters and the bottom-top room where the princess is imprisoned.
"""
"""
intuition:
TC:O(n^2)
SC:O(m*n)
"""
# class Solution:
#     def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:

dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
r = len(dungeon)
c = len(dungeon[0])
#create dp table
dp = [[0 for _ in range (c)] for _ in range (r)]
print (dp)
#initailze the right bottom corner as 1
dp[-1][-1] = 1 
# print (dp)
for i in range (r-2,-1,-1):#handling column and start from the top 
    print (i,c)
    dp[i][c-1] = max(1,dp[i+1][c-1]-dungeon[i+1][c-1])
# print (dp)
for j in range (c-2,-1,-1):#handling row and start from the bottom row 
    print(j,r)
    dp[r-1][j] = max(1,dp[r-1][j+1]-dungeon[r-1][j+1])
# print (dp)
for i in range (r-2,-1,-1):
    for j in range (c-2,-1,-1):
        print(i,j)
        top = max(1,dp[i][j+1]-dungeon[i][j+1])
        print (top)
        left = max(1,dp[i+1][j]-dungeon[i+1][j])
        print (left)
        dp[i][j] = min(top,left)
print (max(1,dp[0][0]-dungeon[0][0]))