"""
1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence

Given a sentence that consists of some words separated by a single space, and a searchWord.

You have to check if searchWord is a prefix of any word in sentence.

Return the index of the word in sentence where searchWord is a prefix of this word (1-indexed).

If searchWord is a prefix of more than one word, return the index of the first word (minimum index). If there is no such word return -1.

A prefix of a string S is any leading contiguous substring of S.

 

Example 1:

Input: sentence = "i love eating burger", searchWord = "burg"
Output: 4
Explanation: "burg" is prefix of "burger" which is the 4th word in the sentence.
Example 2:

Input: sentence = "this problem is an easy problem", searchWord = "pro"
Output: 2
Explanation: "pro" is prefix of "problem" which is the 2nd and the 6th word in the sentence, but we return 2 as it's the minimal index.
Example 3:

Input: sentence = "i am tired", searchWord = "you"
Output: -1
Explanation: "you" is not a prefix of any word in the sentence.
Example 4:

Input: sentence = "i use triple pillow", searchWord = "pill"
Output: 4
Example 5:

Input: sentence = "hello from the other side", searchWord = "they"
Output: -1
 

Constraints:

1 <= sentence.length <= 100
1 <= searchWord.length <= 10
sentence consists of lowercase English letters and spaces.
searchWord consists of lowercase English letters.
"""
"""
inutition:
turn setence into list with bunch of elements
iterate it and check if search word in that element(it has to start at the begining of that element,which is prefix)
TC:O(n)
SC:O(1)
"""
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:

        #edge case
        if not sentence: return -1
        #split the string into list 
        s = sentence.split()
        # print (s)
        for i in range(len(s)):
            m = len(searchWord)
            if s[i][0:m] == searchWord:
                return (i+1)
        return -1
"""
another approach from discussion using startswith() 
"""
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
            for i, w in enumerate(sentence.split(' '), 1):
                if w.startswith(searchWord):
                    return i
            return -1    
sentence = "i love eating burger"
searchWord = "burg"
sol = Solution()
ans = sol.isPrefixOfWord(sentence,searchWord)
print (ans)