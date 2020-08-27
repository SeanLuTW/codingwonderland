"""
673. Number of Longest Increasing Subsequence

Given an unsorted array of integers, find the number of longest increasing subsequence.

Example 1:
Input: [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].
Example 2:
Input: [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.
"""
# class Solution:
#     def findNumberOfLIS(self, nums: List[int]) -> int:
"""
DP sol from discussion
"""
nums = [2,2,2,2,2]
N = len(nums)
if N <= 1: print(N) 
LIS = [1] * N #lengths[i] = longest ending in nums[i]
count = [1] * N #count[i] = number of longest ending in nums[i]

for i in range (1,N):#i run faster than j
    print ("i",i)
    for j in range (0,i):#j will start the iteration from 0 til i
        print ("j",j)
        print ("number faster",nums[i])
        print ("iterate num",nums[j])
        if nums[i]> nums[j]: #means it is increasing
            print ("LIS[i]",LIS[i])
            print ("LIS[j]",LIS[j])
            if LIS[i]==LIS[j]+1:
                print ('test')
                count[i]+=count[j]
            elif LIS[i] < LIS[j]+1:#increasing
                count[i] = count[j]
                LIS[i]=LIS[j]+1#increasing the length from last position
        print ("LIS",LIS)
        print ("count",count)
longest = max(LIS)
print (sum(value for index,value in enumerate(count) if LIS[index] == longest))

"""
self trying using DP 
TC:O(n^2)
SC:O(n)
"""
N = len(nums)
#edge case
if N <=1:print(N) 
LIS  = [1] * N
count = [1] * N
for i in range(1,N):#i run faster than j
    for j in range (0,i):
        if nums[i]>nums[j]:#if i is larger than j which is an increasing trend 
            if LIS[j]>=LIS[i]:#it's a normal case if it's increse trend than it will larger than out default 1
                LIS[i] = LIS[j]+1
                count[i] = count[j]
            elif LIS[j]+1 ==LIS[i]: #if more than 1 LIS(we already update the LIS in that posision, if last posision +1 is equal to current then there are 2 LIS in that posision)
                count[i] += count[j]
print (LIS)
print (count)
longest = max(LIS)
print (sum(value for index,value in enumerate(count) if LIS[index] == longest))