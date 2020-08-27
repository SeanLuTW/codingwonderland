"""
394. Decode String

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
Example 4:

Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"
"""
"""
intuition:
using two stack 
TC:O(N)
SC:O(N)

ref:
https://leetcode.com/problems/decode-string/discuss/699980/Python-Simple-solution-using-2-stacks
"""
# class Solution:
    # def decodeString(self, s: str) -> str:
string= "3[a]2[bc]"
nums =[]
chars = []
num = ""
ans = ""
for i in string:
    # print ("i",i)#fd
    if i.isdigit():
        num+=i
    elif i=="[":
        nums.append(int(num))#get ready to multiple 
        chars.append(ans)
        # print ("nums",nums)#fd
        # print ("ans",ans)#fd
        num = ans = ""#empty num and ans
    elif i=="]":
        print ("ans",ans)
        print ("char",chars)
        print ("nums",nums)
        ans= chars.pop()+nums.pop()*ans 
        print ("ans",ans)
    else:
        ans+=i
print (ans)