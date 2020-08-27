"""
1268. Search Suggestions System

Given an array of strings products and a string searchWord. We want to design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with the searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return list of lists of the suggested products after each character of searchWord is typed. 

 

Example 1:

Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
After typing mou, mous and mouse the system suggests ["mouse","mousepad"]
Example 2:

Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
Example 3:

Input: products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]
Example 4:

Input: products = ["havana"], searchWord = "tatiana"
Output: [[],[],[],[],[],[],[]]
"""
"""
Intuition
In a sorted list of words,
for any word A[i],
all its sugested words must following this word in the list.

For example, if A[i] is a prefix of A[j],
A[i] must be the prefix of A[i + 1], A[i + 2], ..., A[j]

Explanation
With this observation,
we can binary search the position of each prefix of search word,
and check if the next 3 words is a valid suggestion.

TC:O(NlogN) for sorting 
SC:O(logN) for quick sort

ref:
https://leetcode.com/problems/search-suggestions-system/discuss/436674/C%2B%2BJavaPython-Sort-and-Binary-Search-the-Prefix
"""
# class Solution:
    # def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
from bisect import bisect_left
products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"
products = sorted(products)
print (products)
# products.sort()#inplace sorting
ans = []
prefix = ''
i = 0
for c in searchWord:
    prefix+=c
    i = bisect_left(products,prefix,i)
    ans.append([w for w in products[i:i+3] if w.startswith(prefix)])
print (ans)


