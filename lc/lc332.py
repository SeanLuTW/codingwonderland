"""
332. Reconstruct Itinerary

Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:

If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
One must use all the tickets once and only once.
Example 1:

Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
Example 2:

Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
             But it is larger in lexical order.
"""
"""
intuition:
reconstruct the itinerary from smaller to larger in lexical order


"""
# class Solution:
    # def findItinerary(self, tickets: List[List[str]]) -> List[str]:
tickets =[["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
graph = {}
for start,end in tickets:
    if start in graph:
        graph[start].append(end)
    else:
        graph[start] = [end]
# print (graph)
for start in graph.keys():
    graph[start].sort(reverse = True)
# print (graph)
stack = []
ans = []
stack.append("JFK")
while stack:
    element = stack[-1]
    if element in graph and len(graph[element])>0:
        stack.append(graph[element].pop())
    else:
        ans.append(stack.pop())
print (ans)
print (ans[::-1])