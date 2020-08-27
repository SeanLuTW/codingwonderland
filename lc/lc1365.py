"""
1365. How Many Numbers Are Smaller Than the Current Number

Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.

 

Example 1:

Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation: 
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1). 
For nums[3]=2 there exist one smaller number than it (1). 
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
Example 2:

Input: nums = [6,5,4,8]
Output: [2,1,0,3]
Example 3:

Input: nums = [7,7,7,7]
Output: [0,0,0,0]
"""
"""
intuition:
use enumerate to get the index and value 
the smaller number of that certain number is exactly the index 
"""

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range (0,len(nums)):
            countsmaller = 0
            for y in range(0,len(nums)):
                if nums[y]<nums[i]:
                    countsmaller+=1
            ans.append(countsmaller)
        return (ans)


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        nums = [6,5,4,8]
        dic = {}
        for index , value in enumerate(sorted(nums)):
            if value not in dic:
                dic[value] = index
        return (dic[value] for value in nums)