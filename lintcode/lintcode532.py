"""
532. Reverse Pairs
Description
Reverse pair is a pair of numbers (A[i], A[j]) such that A[i] > A[j] and i < j. Given an array, return the number of reverse pairs in the array.

Have you met this question in a real interview?  
Example
Example1

Input:  A = [2, 4, 1, 3, 5]
Output: 3
Explanation:
(2, 1), (4, 1), (4, 3) are reverse pairs
Example2

Input:  A = [1, 2, 3, 4]
Output: 0
Explanation:
No reverse pair
"""
A = [2, 4, 1, 3, 5]
ans = 0
n = len(A)
for i in range(n):
    for j in range(i+1,n):
        if A[i]>A[j]:
            ans+=1
print(ans)