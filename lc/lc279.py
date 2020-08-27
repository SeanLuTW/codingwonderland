"""
279. Perfect Squares

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""
"""
intuition:
see if n can be divided by any square number
square num will be 1,4,9,16...
using BFS will be similiar as find shortest path to 0 
"""
# class Solution:
#     def numSquares(self, n: int) -> int:
n = 12
if n == 1 :
    print (1)
square = []
i = 1 
#build up square list
while i*i <=n:
    square.append(i*i)
    i+=1
pathcount = 0
check = {n}
while check:
    pathcount+=1
    tmp = set()
    for i in check:
        for j in square:
            if i==j:
                print (pathcount)
            if i<j:
                break
            tmp.add(i-j)
    check = tmp
print (pathcount)