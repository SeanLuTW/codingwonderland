"""
1189. Maximum Number of Balloons
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.
"""
#ballon
text = "nlaebolko"
word = 'balloon'
from collections import Counter 
cnttext = Counter(text)
print (cnttext)
cntb = Counter(word)
print (cntb)


print (min([cnttext[i]/ cntb[i] for i in cntb]))

"""
Time: O(text.length()), space: O(1).
"""
#discussion idea 
word = "balloon"
print ( min(text.count(key)//word.count(key) for key in set(word) ))