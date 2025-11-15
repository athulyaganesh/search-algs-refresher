graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
    } 

def dfs_iterative(graph, start):
    stack = [start]
    visited = set() 
    
    while stack: 
        currentNode = stack.pop()
        if currentNode in visited: 
            continue  
        visited.add(currentNode) 
        print(currentNode)
        for n in graph[currentNode]: 
            if n not in visited and n not in stack: 
                stack.append(n) 
                
dfs_iterative(graph, 'A')