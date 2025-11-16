def bfs_recursive(graph, queue, visited):  
    if not queue: 
        return 
    if not visited: 
        return 
    
    curNode = queue.pop(0)
    visited.add(curNode)
    print(curNode)
    
    for n in graph[curNode]: 
        queue.append(n)
    
    bfs_recursive(graph, queue, visited)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
    } 

start = 'A'
bfs_recursive(graph, [start], {start})           
        