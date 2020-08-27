"""
1078. Occurrences After Bigram

Given words first and second, consider occurrences in some text of the form "first second third", where second comes immediately after first, and third comes immediately after second.

For each such occurrence, add "third" to the answer, and return the answer.

 

Example 1:

Input: text = "alice is a good girl she is a good student", first = "a", second = "good"
Output: ["girl","student"]
Example 2:

Input: text = "we will we will rock you", first = "we", second = "will"
Output: ["we","rock"]

        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]

"""
text = "we will we will rock you"
first = "we"
second = "will"
if not text:
    print ('')
ans = []
text = text.split()
# print (text)
for i in range(2,len(text)):
    if text[i-2] == first and text[i-1] == second:
        ans.append(text[i])
print (ans)