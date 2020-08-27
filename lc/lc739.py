"""
739. Daily Temperatures

Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].
"""
"""
need to remember the index and use index diff to get the value

"""
#idea from discussion using stack

"""
TC:O(N), N is the length of T
SC:O(W),W is the number of allowed values for T[i]. Each index gets pushed and popped at most once from the stack.
The size of the stack is bounded as it represents strictly increasing temperatures.
"""
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        
        # T = [73, 74, 75, 71, 69, 72, 76, 73]
        ans = [0]*len(T)
        stack = []#store index 
        for index, value in enumerate(T):
            while stack and T[stack[-1]]< value:#top in stack less than value  
                prev_index = stack.pop()
                ans[prev_index] = index - prev_index
            stack.append(index)#if current is greater than future put it into stack 
            return ans