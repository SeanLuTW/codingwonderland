"""
1247. Minimum Swaps to Make Strings Equal

You are given two strings s1 and s2 of equal length consisting of letters "x" and "y" only. Your task is to make these two strings equal to each other. You can swap any two characters that belong to different strings, which means: swap s1[i] and s2[j].

Return the minimum number of swaps required to make s1 and s2 equal, or return -1 if it is impossible to do so.

 

Example 1:

Input: s1 = "xx", s2 = "yy"
Output: 1
Explanation: 
Swap s1[0] and s2[1], s1 = "yx", s2 = "yx".
Example 2: 

Input: s1 = "xy", s2 = "yx"
Output: 2
Explanation: 
Swap s1[0] and s2[0], s1 = "yy", s2 = "xx".
Swap s1[0] and s2[1], s1 = "xy", s2 = "xy".
Note that you can't swap s1[0] and s1[1] to make s1 equal to "yx", cause we can only swap chars in different strings.
Example 3:

Input: s1 = "xx", s2 = "xy"
Output: -1
Example 4:

Input: s1 = "xxyyxyxyxx", s2 = "xyyxyxxxyx"
Output: 4
 

Constraints:

1 <= s1.length, s2.length <= 1000
s1, s2 only contain 'x' or 'y'.
"""
"""
intuition:
idea from discussion
xx/yy need 1 step
sy/yx need 2 steps 
base on the question provided, we set up the condition 
TC:O(n)

ref:
https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/discuss/455654/Python-simple-code-using-sets
"""
s1 = 'xy'
s2 = 'yx'

check = set()
swap = 0
for i in range (len(s1)):
    if s1[i]!=s2[i]:
        combine = s1[i] +s2[i]
        # print (combine)
        if combine in check:
            check.remove(combine)
            swap+=1
        else:
            check.add(combine)

print (check)
print (swap)
if len(check) ==1:
    print (-1)
elif len(check) == 2:
    print (swap+2)
else:
    print (swap)