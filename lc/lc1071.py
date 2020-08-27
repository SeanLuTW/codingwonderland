"""
1071. Greatest Common Divisor of Strings

For strings S and T, we say "T divides S" if and only if S = T + ... + T  (T concatenated with itself 1 or more times)

Return the largest string X such that X divides str1 and X divides str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"reaple
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
"""

if len(str1) > len(str2):
    longstr, shortstr = str1, str2

else:
    longstr, shortstr = str2, str1

if shortstr == '':
    print (longstr)

if shortstr not in longstr:
    print ('')

print (self.gcdOfStrings(shortstr, longstr.replace(shortstr, '')))

