"""
961. N-Repeated Element in Size 2N Array

In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.

Return the element repeated N times.

 

Example 1:

Input: [1,2,3,3]
Output: 3
Example 2:

Input: [2,1,2,5,3,2]
Output: 2
Example 3:

Input: [5,1,5,2,5,3,5,4]
Output: 5
"""
#findout the total count of nuber where it is N/2

#approach 1 #time  exceeded
# A = [2,1,2,5,3,2]
# num = len(A)/2
# for i in set(A):
#     if A.count(i) == num:
#         print (i)

#approach 2
# A = [2,1,2,5,3,2]
# from collections import Counter
# num = len(A)/2
# cnta = Counter(A)
# for i in cnta:
#     if cnta[i] == num:
#         print (i)

#discussion ans         
A = [2,1,2,5,3,2]
d = {}
for elements in A:
    if elements in d:
        print (elements)
    else:
        d[elements] = True
print (d)