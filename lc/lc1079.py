"""
1079. Letter Tile Possibilities

You have a set of tiles, where each tile has one letter tiles[i] printed on it.  Return the number of possible non-empty sequences of letters you can make.

 

Example 1:

Input: "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
Example 2:

Input: "AAABBC"
Output: 188
 

Note:

1 <= tiles.length <= 7
tiles consists of uppercase English letters.
"""
tiles = 'AAB'
#idea from disscussion 
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        
        from itertools import permutations
        ans = set()
        for i in range (1,len(tiles)+1):
            tmp = permutations((tiles),i)
            # print (list(tmp)) #fordebug
            [ans.add(x) for x in tmp]
        return (len(ans))