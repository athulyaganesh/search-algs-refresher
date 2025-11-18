'''
Minimum Spanning Tree: Prim's 
GOAT: https://www.youtube.com/watch?v=4ZlRH0eK-qQ Abdul Bari 
'''
import heapq  

def prims(graph, start = 0):
    visited = set() 
    minHeap = [(start, 0)] # vertex, weight 
    mstCost = 0 
    
    while minHeap: 
        v, w = heapq.heappop(minHeap)
        
        if v in visited: 
            continue  
        visited.add(v)
        
        mstCost += w 
        
        for ver, weight in graph[v]: 
            if ver not in visited: 
                heapq.heappush(minHeap, (ver, weight)) 
    
    if len(visited) != len(graph): 
        return None 
    return mstCost
        


# Graph as adjacency list:
# 0---1 (weight 2)
# 0---2 (weight 3)
# 1---2 (weight 1)
graph = {
    0: [(1, 2), (2, 3)],
    1: [(0, 2), (2, 1)],
    2: [(0, 3), (1, 1)]
}

min_cost = prims(graph)
print("Minimum cost of MST:", min_cost)