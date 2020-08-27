"""
1122. Relative Sort Array

Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.  Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.

 

Example 1:

Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]

"""

arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
# k = {v: i for i, v in enumerate(B)}
# print (k)

# print( sorted(A, key=lambda a: k.get(a, 1000 + a)))



# print (sorted(arr1,key = lambda x: for x in arr2))
from collections import Counter
ans, cnt = [], Counter(arr1)         # Count each number in arr1
print (cnt)
for i in arr2:
    if cnt[i]: 
        ans.extend([i]*cnt[i])
        cnt.pop(i)      # Sort the common numbers in both arrays by the order of arr2. 
print (cnt)
for i in range(1001):               
    if cnt[i]: ans.extend([i] * cnt.pop(i))      # Sort the numbers only in arr1.
print (ans)