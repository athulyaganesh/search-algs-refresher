'''
Finds the shortest path from one starting node to all other nodes in a weighted graph with non-negative edge weights. 
Neetcode: https://www.youtube.com/watch?v=XEb7_z5dG3c 

# Graph (n = 5, src = 0)
#
#        (10)
#    0 --------> 1
#    | \         \
# (3)|  \          \ (2)
#    |   \          \
#    v    v          v
#    2 -> 1 -> 3 -> 4
#   (4)   |    ^    ^
#         |    |    |
#        (2)  (8)  (5)
#         v    |    |
#         4 <--+----+
#
# Edges:
# 0 -> 1 (10)
# 0 -> 2 (3)
# 2 -> 1 (4)
# 1 -> 3 (2)
# 2 -> 3 (8)
# 2 -> 4 (2)
# 3 -> 4 (5)

'''
import heapq 

n = 5
edges = [[0,1,10], [0,2,3], [1,3,2], [2,1,4], [2,3,8], [2,4,2], [3,4,5]]
src = 0

def djikstras_algorithm(n, edges, src):
    
    shortest = {} 
    adjList = {} 
    
    adjList = {i: [] for i in range(n)} 
    for s, d, weight in edges:
        adjList[s].append([weight, d])
        
    minHeap = [[0, src]] 
    while minHeap: 
        w1, n1 = heapq.heappop(minHeap)
        
        if n1 in shortest: 
            continue 
        
        shortest[n1] = w1 
        
        for w2, n2 in adjList[n1]: 
            if n2 not in shortest: 
                heapq.heappush(minHeap, [w2 + w1, n2])
        
    for i in range(n): 
        if i not in shortest: 
            shortest[i] = -1 
    return shortest 

print(djikstras_algorithm(n, edges, src))
