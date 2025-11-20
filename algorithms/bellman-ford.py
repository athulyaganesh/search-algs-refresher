def bellman_ford(graph, source):
    '''
    https://www.youtube.com/watch?v=FtN3BYH2Zes
    djikstra's but better bc it works with negative numbers too
    doesnt work onnegative weight  cycles
    '''
    """
    Computes the shortest paths from a source vertex to all other vertices
    in a weighted digraph using the Bellman-Ford algorithm.

    Args:
        graph (dict): A dictionary representing the graph.
                      Keys are vertices, values are dictionaries of neighbors
                      and their respective edge weights.
                      Example: {'A': {'B': -1, 'C': 4}, 'B': {'C': 3}}
        source: The starting vertex for shortest path calculations.

    Returns:
        dict: A dictionary containing the shortest distances from the source
              to all reachable vertices.
              Returns None if a negative-weight cycle is detected.
    """
    # Step 1: Initialize distances
    distances = {vertex : float('inf') for vertex in graph} 
    distances[source] = 0

    # Step 2: Relax edges |V| - 1 times
    numEdges = len(distances) - 1 
    
    for i in range(numEdges - 1): 
        for u in graph: 
            for v, weight in graph[u].items(): 
                if distances[u] + weight < distances[v]: 
                    distances[v] = distances[u] + weight 

    # Step 3: Check for negative-weight cycles
    for u in graph: 
        for v, weight in graph[u].items(): 
            if distances[u] + weight < distances[v]: 
                return "CYCLE DETECTED"
    return distances 
    
    return distances  
# Example Usage:
if __name__ == "__main__":
    graph1 = {
        'A': {'B': -1, 'C': 4},
        'B': {'C': 3, 'D': 2, 'E': 2},
        'C': {},
        'D': {'B': 1, 'C': 5},
        'E': {'D': -3}
    }
    source1 = 'A'
    shortest_distances1 = bellman_ford(graph1, source1)
    if shortest_distances1:
        print(f"Shortest distances from '{source1}': {shortest_distances1}")

    print("\n--- Example with a negative cycle ---")
    graph_negative_cycle = {
        'A': {'B': 1},
        'B': {'C': -1},
        'C': {'A': -1}
    }
    source_negative_cycle = 'A'
    shortest_distances_negative_cycle = bellman_ford(graph_negative_cycle, source_negative_cycle)
    if shortest_distances_negative_cycle:
        print(f"Shortest distances from '{source_negative_cycle}': {shortest_distances_negative_cycle}")