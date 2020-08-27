"""
322. Coin Change

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
"""
"""
intuition:
using the formula of dp[i] = min(dp[i],dp[i-coin]+1)
                                dp[i]->with pick coin
                                dp[i-coin]-> remain total
TC:O(S*n)
Sc:O(S)

ref:
https://www.youtube.com/watch?v=NJuKJ8sasGk
"""
# class Solution:
#     def coinChange(self, coins: List[int], amount: int):
amount = 11
coins = [1,2,5]
dp = [float('inf')]*(amount+1)
dp[0] = 0#initial the first element 
for coin in coins:
    print ("coin",coin)
    for i in range (coin,amount+1):
        # print ("i",i)
        # print (dp[i])
        # print (dp[i-coin])
        dp[i] = min(dp[i],dp[i-coin]+1)# plus one is coz you pick up the coin
        # print (dp[i])
print (dp[amount] if dp[amount]!=float('inf') else -1)