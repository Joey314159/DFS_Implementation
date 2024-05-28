
#Iterative Method
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

dfs(graph, '0')
