"""
1128. Number of Equivalent Domino Pairs

Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a==c and b==d), or (a==d and b==c) - that is, one domino can be rotated to be equal to another domino.

Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].

 

Example 1:

Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
Output: 1
 

Constraints:

1 <= dominoes.length <= 40000
1 <= dominoes[i][j] <= 9
"""

"""
intuition:
this problem is similiar to 2 sum 
the key for this problem is the forluma min(i,j)*10 + max(i,j)
TC:O(n) n = dominoes.length.
SC:O(45) Since 1 <= dominoes[i][j],there are at most 9 * (9 + 1) / 2 = 45 encodings.
ref:
https://leetcode.com/problems/number-of-equivalent-domino-pairs/discuss/339969/JavaPython-3-O(n)-code-with-brief-explanation-and-analysis.
"""
dominoes = [[1,2],[2,1],[3,4],[5,6]]
dic = {}
count = 0
for i, j in dominoes:
    key = min(i,j)*10 + max(i,j)
    if key in dic:
        count +=dic[key]
        dic[key]+=1
    else:
        dic[key] = 1
print (count)