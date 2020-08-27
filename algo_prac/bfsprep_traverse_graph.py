# def bfs(graph, start):
#     visited = set()
#     queue = [start]
#     while queue:
#         vertex = queue.pop(0)
#         if vertex not in visited:
#             visited.add(vertex)
#             queue.extend(graph[vertex] - visited)
#     return visited

"""
Traversing a graph
"""
def bfs_connected_component(graph, start):
    # keep track of all visited nodes
    explored = []
    # keep track of nodes to be checked
    queue = [start]
    # keep looping until there are nodes still to be checked
    while queue:
        # pop shallowest node (first node) from queue
        node = queue.pop(0)
        if node not in explored:
            # add node to list of checked nodes
            explored.append(node)
            neighbours = graph[node]

            # add neighbours of node to queue
            for neighbour in neighbours:
                queue.append(neighbour)
    print (explored)

# sample graph implemented as a dictionary

graph = {'A': ['B', 'C', 'E'],
         'B': ['A','D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B'],
         'E': ['A', 'B','D'],
         'F': ['C'],
         'G': ['C']}

bfs_connected_component(graph,'A')
# returns ['A', 'B', 'C', 'E', 'D', 'F', 'G']

"""
Tip: To make the code more efficient, you can use the deque object from the collections module instead of a list, for implementing queue.
This way you can use the popleft() method instead of the  pop(0) built-in function on queue. This will result in a quicker code as popleft()has a time complexity of O(1) while pop(0) has O(n).
"""


