"""
300. Longest Increasing Subsequence

Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
"""
"""
intuition:
DP:
TC:O(n^2)
SC:O(n)

BS:
TC:O(nlogn)
SC:O()

ref:
https://www.youtube.com/watch?v=7DKFpWnaxLI
"""
"""
DP Solution
"""
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         if not nums:return 0
#         dp  = [1]*len(nums)
#         for i in range (len(nums)):
#             for j in range (0,i):
#                 if nums[i]> nums[j]:
#                     dp[i] = max(dp[i],dp[j]+1)#adding 1 which is the current last num it self  
#         return max(dp)
"""
binary search 
bisect.bisect_left(a,x, lo=0, hi=len(a)) :
查找在有序列表 a 中插入 x 的index。lo 和 hi 用于指定列表的区间，默认是使用整个列表。如果 x 已经存在，在其左边插入。返回值为 index。
"""
import bisect
nums = [10,9,2,5,3,7,101,18]
dp = []
for i in nums:
    print ("num",i)
    ind = bisect.bisect_left(dp,i)#the bisect function will return index 
    print ("index",ind)
    print ("len",len(dp))
    if ind == len(dp):#the case we are looking which is increasing number
        dp.append(i)
    else:#if i is smaller
        dp[ind] = i 
    print (dp)
print (len(dp))