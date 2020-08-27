"""
697. Degree of an Array

Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.

Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6
"""
#idea from discussion 
nums = [1,2,2,3,1,4,2]
from collections import Counter
firstappear, lastappear = {}, {}
for i, v in enumerate(nums):
    # firstappear.setdefault(v, i)
    firstappear[v] = firstappear.get(v,i) 
    lastappear[v] = i
print (firstappear)
print (lastappear)
c = Counter(nums)
print (c)
degree = max(c.values())
print (degree)
print(min(lastappear[v] - firstappear[v] + 1 for v in c if c[v] == degree))

