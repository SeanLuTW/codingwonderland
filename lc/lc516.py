"""
516. Longest Palindromic Subsequence

"""
"""
intuition:
The tricky part is representing this in a data structure for our memoization, and we'll go with an intial matrix to represent the example above:
From then on we simply build our table with the following logic, if the current row character matches the column character,
then we take value from row+1 and column-1, and increment by 2.
Why? Suppose we have BCCCB, if we're looking BCCCB vs CCCB, BCCCB has a length of 5 that is a paldinrome, while CCCB has 3 (CCC), so the difference is 2.
__B B B A B
B 1
B 0 1
B 0 0 1
A 0 0 0 1
B 0 0 0 0 1

ref:
https://leetcode.com/problems/longest-palindromic-subsequence/discuss/216717/Python-DP-solution-w-explanation
https://www.google.com/search?q=2d+matrix&tbm=isch&ved=2ahUKEwj4gMPOisPpAhUXjJ4KHUF3CswQ2-cCegQIABAA&oq=2D+ma&gs_lcp=CgNpbWcQARgBMgIIADICCAAyAggAMgIIADIECAAQHjIECAAQHjIECAAQHjIECAAQHjIECAAQHjIECAAQHlD2-Z8BWMiBoAFg3pCgAWgAcAB4AIABQ4gBtgKSAQE1mAEAoAEBqgELZ3dzLXdpei1pbWc&sclient=img&ei=fnjFXvhJl5j6BMHuqeAM#imgrc=6jIFCe6XHV0d8M

2D array matrix

[0][0]|[0][1]
______|______
[1][0]|[1][1]
     

TC:O(n^2)
SC:O(n)
"""
# s = 'bbbab'
# if s == s[::-1]:
#     print (len(s))
# dp = [[0 for j in range(len(s))]for i in range (len(s))]#create 2D array 
# # print (dp)
# for i in range (len(s)-1,-1,-1):
#     print ("i",i)
#     # dp[i][i]=1
#     for j in range (i+1,len(s)):
#         print ("j",j)
#         if s[i]==s[j]:
#             dp[i][j] = 2+dp[i+1][j-1]#get the value from left bottom
#         else:
#             dp[i][j] = max(dp[i+1][j],dp[i][j-1])#f it doesn't match, then we take the max between the left value, and the bottom value of our current position. 
# print (dp)
# print (dp[0][len(s)-1])

s= 'bbbab'
dp = [[0]*len(s) for i in range (len(s))]
print (dp)

k = 0
while k < len(s):
    for i in range (len(s)-k):
        j = i+k
        if i==j:
            dp[i][j]=1
        elif s[i]==s[j]:
            dp[i][j] = dp[i+1][j-1]+2#rightbottom +2
        else:
            dp[i][j] = max(dp[i][j-1],dp[i+1][j]) #left vs bottom of current position

    k+=1
print (dp[0][len(s)-1])

