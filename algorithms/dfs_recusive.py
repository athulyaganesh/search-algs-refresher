#DFS: Recursive Implementation in Python
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
    } 

def dfs_recursive(graph, node, visited): 
    if visited is None: 
        visited = set()
    
    visited.add(node)
    print(node)
    
    for n in graph[node]:
        if n not in visited: 
            dfs_recursive(graph, n, visited)
    
    return visited 

dfs_recursive(graph, 'A', set())