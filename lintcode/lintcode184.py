"""
184. Largest Number
Given a list of non negative integers, arrange them such that they form the largest number.

Example
Example 1:

Input:[1, 20, 23, 4, 8]
Output:"8423201"
Example 2:

Input:[4, 6, 65]
Output:"6654"
Challenge
Do it in O(nlogn) time complexity.

Notice
The result may be very large, so you need to return a string instead of an integer.
"""
nums = [1, 20, 23, 4, 8]
new = sorted(nums,key = lambda x:str(x)[0])[::-1]
# print (new)
ans = [str(i) for i in new]
print (''.join(ans))