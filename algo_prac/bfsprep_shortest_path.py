# def bfs_shortest_path(graph, start, goal):
#     # keep track of explored nodes
#     explored = []
#     # keep track of all the paths to be checked
#     queue = [[start]]#path records

#     if start == goal:
#         print ("start = goal")
#     # keeps looping until all possible paths have been checked    
#     while queue:
#         # pop the first path from the queue
#         path = queue.pop(0)
#         # get the last node from the path
#         node = path[-1]
#         if node not in explored:
#             neighbours = graph[node]
#             # go through all neighbour nodes, construct a new path and
#             # push it into the queue
#             for i in neighbours:
#                 new_path = list(path)
#                 new_path.append(i)
#                 queue.append(new_path)
#                 # return path if neighbour is goal
#                 if i == goal:
#                     print(new_path)
#             # mark node as explored
#             explored.append(node)
#     # print("So sorry, but a connecting path doesn't exist :(")



# # sample graph implemented as a dictionary
# graph = {'A': ['B', 'C', 'E'],
#          'B': ['A','D', 'E'],
#          'C': ['A', 'F', 'G'],
#          'D': ['B'],
#          'E': ['A', 'B','D'],
#          'F': ['C'],
#          'G': ['C']}

# bfs_shortest_path(graph, 'D', 'A')  
# returns ['G', 'C', 'A', 'B', 'D']


def bfs_short_path(graph, start, end):
    visited = []
    queue = [[start]]

    while queue:
        path = queue.pop(0)
        print (path)
        node = path[-1]
        print(node)
        if node not in visited:
            neighbours = graph[node]
            for i in neighbours:
                newpath = list(path)
                print (newpath)
                newpath.append(i)
                queue.append(newpath)
                if i ==end:
                    print(newpath)
            visited.append(node)
    print (queue)

graph = {'A': ['B', 'C', 'E'],
         'B': ['A','D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B'],
         'E': ['A', 'B','D'],
         'F': ['C'],
         'G': ['C']}

bfs_short_path(graph, 'A', 'F')  