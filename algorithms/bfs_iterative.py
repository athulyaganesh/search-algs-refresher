def bfs_iterative(graph, start):
    visited = set() 
    queue = [start] 
    
    while queue: 
        curNode = queue.pop(0)
        if curNode in visited: 
            continue 
        visited.add(curNode)
        print(curNode)
        
        for node in graph[curNode]: 
            if node not in queue and node not in visited: 
                queue.append(node)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
    } 

bfs_iterative(graph, 'A')           
        