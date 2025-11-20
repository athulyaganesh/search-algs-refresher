def top_sort(graph):
    indegrees = {node : 0 for node in graph}
    
    for node in graph: 
        nei = graph[node] 
        for n in nei: 
            indegrees[n] += 1 
    
    q = [] 
    res = [] 
    count = 0
    
    for node in graph: 
        if indegrees[node] == 0: 
            q.append(node)
    
    while len(q): 
        curNode = q.pop(0)
        
        res.append(curNode) 
        count += 1 
        
        for n in graph[curNode]: 
            indegrees[n] -= 1 
            if indegrees[n] == 0: 
                q.append(n) 
    
    if len(res) != count: 
        return "CYCLE DETECTED"
    return res 


graph = {
    'A' : ['B', 'C'], 
    'B' : ['D'], 
    'C' : ['D'], 
    'D' : ['E'], 
    'E' : [] 
}

print(top_sort(graph))