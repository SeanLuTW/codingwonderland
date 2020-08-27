"""
509. Fibonacci Number
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
Given N, calculate F(N).

 

Example 1:

Input: 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:

Input: 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
Example 3:

Input: 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
"""
#approach 1 using recursion 
class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N <= 1:
            return N
        else:
            return self.fib(N-1) + self.fib(N-2)

#approach 2 using Top Down with memo
class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N <=1 :
            return N
        self.cache = {0:0, 1:1}
        return self.Memoize(N)
        
    def Memoize(self, N):
        if N in self.cache.keys():
            return self.cache[N]
        self.cache[N] = self.Memoize(N-1) + self.Memoize(N-2)
        return self.Memoize(N)

#approach 3  Bottom-Up Approach using Memoization fastest
class Solution:
    def fib(self, N):
        if N <= 1:
            return N
        return self.memoize(N)

    def memoize(self, N):
        cache = {0: 0, 1: 1}

        # Since range is exclusive and we want to include N, we need to put N+1.
        for i in range(2, N+1):
            cache[i] = cache[i-1] + cache[i-2]

        return cache[N]
#approach 3-1  Bottom-Up Approach using Memoization fastest

class Solution:
    def fib(self, N):
        if N <= 1:
            return N
        return self.memoize(N)

    def memoize(self, N):
        self.cache = {0: 0, 1: 1}

        # Since range is exclusive and we want to include N, we need to put N+1.
        for i in range(2, N+1):
            self.cache[i] = self.cache[i-1] + self.cache[i-2]

        return self.cache[N]