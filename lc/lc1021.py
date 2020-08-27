"""
1021. Remove Outermost Parentheses

A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.

A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.

Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.

 

Example 1:

Input: "(()())(())"
Output: "()()()"
Explanation: 
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
Example 2:

Input: "(()())(())(()(()))"
Output: "()()()()(())"
Explanation: 
The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".
Example 3:

Input: "()()"
Output: ""
Explanation: 
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".
"""

S = "(()())(())"
"""
Explanation:
opened count the number of opened parenthesis.
Add every char to the result,
unless the first left parenthesis,
and the last right parenthesis.
"""
#idea from solution 
# res, opened = [], 0
# for c in S:
#     if c == '(' and opened > 0: 
#         res.append(c)
#     if c == ')' and opened > 1: 
#         res.append(c)
#     if c == '(': 
#         opened += 1 
#     else: 
#         opened-=1
    
#     print (res)
# print (opened)
# print ("".join(res))

S = "(()())(())"
count = 0
element = ""
result = ""

for c in S:
    element += c
    if c == "(":
        count += 1
    elif c == ")":
        count -= 1

    if count == 0:
        print (element)
        print (element[1:-1])
        result += element[1:-1]
        element = ""

print (result)
