"""
922. Sort Array By Parity II

Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

You may return any answer array that satisfies this condition.

 

Example 1:

Input: [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.

"""
#approach1
#index matching the value in the element
# A = [4,2,5,7]
# ans = [0]*len(A)

# #handling the evne option 
# e= 0 
# for i,v in enumerate(A):
#     if v%2 == 0:
#         ans[e] = v
#         e+=2

# #handling the odd option

# o = 1
# for i,v in enumerate(A):
#     if v %2 !=0:
#         ans[o] = v
#         o+=2
# print (ans)
"""
TC:O(N)
SC:O(N)
"""
#approach2
A = [4,2,5,7]
ans = [0]*len(A)
e = 0 
o = 1 
for i, v in enumerate(A):
    if v%2 == 0:
        ans[e] = v
        e+=2
    elif v %2 !=0:
        ans[o] = v
        o+=2
print (ans)