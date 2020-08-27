"""
1282. Group the People Given the Group Size They Belong To

There are n people whose IDs go from 0 to n - 1 and each person belongs exactly to one group. Given the array groupSizes of length n telling the group size each person belongs to, return the groups there are and the people's IDs each group includes.

You can return any solution in any order and the same applies for IDs. Also, it is guaranteed that there exists at least one solution. 

 

Example 1:

Input: groupSizes = [3,3,3,3,3,1,3]
Output: [[5],[0,1,2],[3,4,6]]
Explanation: 
Other possible solutions are [[2,1,6],[5],[0,4,3]] and [[5],[0,6,2],[4,3,1]].
Example 2:

Input: groupSizes = [2,1,3,3,3,2]
Output: [[1],[0,5],[2,3,4]]
 

Constraints:

groupSizes.length == n
1 <= n <= 500
1 <= groupSizes[i] <= n
"""
"""
intuition:
we need to have record of the number in the list appear times and it's following index
output should be like{1:[1],2:[0,5],3:[2,3,4]}
"""
# class Solution:
#     def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
# from collections import defaultdict
# groupSizes = [2,1,3,3,3,2]
# count = {}
# print (count)
# ans = []
# for i ,j in enumerate(groupSizes):
#     count[j]+= [i]
#     if len(count[j])== j:
#         ans+=[count[j]]
#         count[j] = []
# print (ans)



groupSizes = [2,1,3,3,3,2]
from collections import defaultdict
count  = defaultdict(list)# in the count dictionary the key would be number and value would be index list 
ans = []
for index, value in enumerate(groupSizes):
    print (index)
    print (value)
    count[value]+=[index]
    if len(count[value]) == value:
        ans+=[count[value]]#which will add it's index 
        count[value] = []
print (ans)