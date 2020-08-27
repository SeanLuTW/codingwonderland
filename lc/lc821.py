"""
821. Shortest Distance to a Character

Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
"""
S = "loveleetcode"
C = "e"
# result = []
        
# positions = [i for i, letter in enumerate(S) if letter == C]#find out the char position
# print (positions)
# for i, letter in enumerate(S):
#     result.append(min([abs(position - i) for position in positions]))

# print(result)

positions = [index for index, letter in enumerate(S) if letter ==C]
ans = []
print (positions)
for index, letter in enumerate(S):
    ans.append(min(abs(position-index) for position in positions))


print (ans)

positions = [index for index, letter in enumerate(S) if letter ==C]
ans = []
for index, letter in enumerate(S):
    ans.append(min(abs(position-index) for position in positions))