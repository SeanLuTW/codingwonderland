"""
1287. Element Appearing More Than 25% In Sorted Array
Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time.

Return that integer.

 

Example 1:

Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6
"""
# class Solution:
#     def findSpecialInteger(self, arr: List[int]) -> int:
from collections import Counter
arr = [1,2,2,6,6,6,6,7,10]
percentage = len(arr)*0.25
# print (percentage)
countarr = Counter(arr)
# print (countarr)
ans = list(str(i) for i in countarr if countarr[i]>percentage)
# print (list(i for i in countarr if countarr[i]>percentage))
print (int(''.join(ans)))
