"""
1013. Partition Array Into Three Parts With Equal Sum

Given an array A of integers, return true if and only if we can partition the array into three non-empty parts with equal sums.

Formally, we can partition the array if we can find indexes i+1 < j with (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1])

 

Example 1:

Input: A = [0,2,1,-6,6,-7,9,1,2,0,1]
Output: true
Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
Example 2:

Input: A = [0,2,1,-6,6,7,9,-1,2,0,1]
Output: false
Example 3:

Input: A = [3,3,6,5,-2,2,5,1,-9,4]
Output: true
Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
"""
"""
intuition:
total num in the array % 3 should be no remain 
total num //3 can find out each segement average value
TC:O(n)
SC:O(1)
"""
class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        A = [3,3,6,5,-2,2,5,1,-9,4]
        average = sum(A)//3
        remain = sum(A)%3
        eachpartsum = 0
        count = 0
        # print (average)#fd
        # print (remain)#fd
        if len(A) ==3:print (A[0]==A[1]==A[2])
        for i in A:
            eachpartsum+=i
            if eachpartsum == average:
                count+=1
                eachpartsum = 0#reset part for next segement
        # print (eachpartsum)#fd
        # print (count)#fd
        # print (remain)#fd
        print (remain==0 and count>=3 and eachpartsum ==0)
"""
NO calculate remain approach
"""
class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        if len(A)== 3:return(A[0]==A[1]==A[2])
        average = sum(A)//3
        eachpartsum = 0
        count = 0

        for i in A:
            eachpartsum+=i
            if eachpartsum == average:
                count+=1
                eachpartsum = 0#reset part for next segement
        return (count>=3 and eachpartsum ==0)