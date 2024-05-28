
#Iterative Method
#I still need to create a stack so it can have one possible output as opposed to many
def dfs(graph, start, visited=None):
    if visited is None:#Marking none as visited first
        visited = set()#Setting some nodes to create an edge
    visited.add(start)#Starting the code

    print(start)

    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

graph = {'0': set(['1', '2', '3']),
         '1': set(['0', '2']),
         '2': set(['0','1','4']),
         '3': set(['0']),
         '4': set(['2'])}

dfs(graph, '0')#Calling the DFS in order to start working, I may come back and implement it with the stack
