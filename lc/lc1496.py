"""
1496. Path Crossing

Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

Return True if the path crosses itself at any point, that is, if at any time you are on a location you've previously visited. Return False otherwise.

 
"""
"""
intuition:
TC:O(n)
"""
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x = y =0
        set ={(0,0)}
        for i in path:
            if i=='N':
                y+=1
            elif i=='E':
                x+=1
            elif i=='W':
                x-=1
            else:
                y-=1
            if (x,y) in set:
                return (True)
            set.add((x,y))
        return (False)
