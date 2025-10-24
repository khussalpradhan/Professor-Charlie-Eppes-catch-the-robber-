import heapq

def dijkstra_sssp(graph, start_node, all_nodes):
    """
    Implements Dijkstra's SSSP algorithm using a min-heap.
    
    Args:
        graph (dict): The graph represented as an adjacency list.
                      Format: {u: [(v, weight), ...]}
        start_node (int): The source vertex.
        all_nodes (range): A range object of all node IDs (e.g., range(1, 23))

    Returns:
        tuple: (distances, parents)
               distances (dict): Shortest path distances from start_node.
               parents (dict): Parent pointers to reconstruct the paths.
    """
    
    # Initialize distances to infinity for all nodes
    distances = {node: float('inf') for node in all_nodes}
    # Parent pointers to reconstruct paths
    parents = {node: None for node in all_nodes}
    
    # Source node distance is 0
    distances[start_node] = 0
    
    # The min-priority queue. Stores tuples of (distance, node).
    pq = [(0, start_node)]
    
    # A set to track nodes for which we have finalized the shortest path.
    visited = set()

    while pq:
        # Extract the node with the smallest distance
        current_dist, u = heapq.heappop(pq)

        # If we already finalized this node, skip it.
        if u in visited:
            continue
            
        visited.add(u)

        # Check all neighbors of the current node
        if u in graph:
            for v, weight in graph[u]:
                # Only process nodes we haven't finalized
                if v not in visited:
                    new_dist = current_dist + weight
                    
                    # This is the "Relaxation" step
                    if new_dist < distances[v]:
                        distances[v] = new_dist
                        parents[v] = u
                        # This push operation is our "decrease-key"
                        heapq.heappush(pq, (new_dist, v))
                        
    return distances, parents

# --- Main Program to Run ---

# 1. Define the graph input
# This is the adjacency list for the graph you specified
my_graph = {
    1: [(2, 1), (11, 1)],
    2: [(1, 1), (3, 1), (21, 1)],
    3: [(2, 1), (4, 1), (8, 2)],
    4: [(3, 1), (5, 1)],
    5: [(4, 1), (6, 2), (7, 1), (22, 1)],
    6: [(5, 2), (7, 1)],
    7: [(5, 1), (6, 1), (8, 1)],
    8: [(7, 1), (9, 1), (3, 2)],
    9: [(8, 1), (10, 1), (19, 1)],
    10: [(9, 1), (11, 1), (18, 2)],
    11: [(1, 1), (10, 1), (12, 2), (17, 1)],
    12: [(11, 2), (13, 2)],
    13: [(12, 2), (14, 2), (21, 1)],
    14: [(13, 2), (15, 1), (20, 1), (16, 1)],
    15: [(14, 1)],
    16: [(17, 2), (14, 1)],
    17: [(11, 1), (16, 2), (18, 2)],
    18: [(10, 2), (17, 2)],
    19: [(9, 1)],
    20: [(14, 1), (21, 2), (22, 1)],
    21: [(2, 1), (13, 1), (20, 2), (22, 2)],
    22: [(5, 1), (20, 1), (21, 2)]
}

# 2. Define the parameters
start_node = 1
all_nodes = range(1, 23) # For nodes 1 through 22
target_destinations = [6, 8, 9, 15, 16, 22]

# 3. Run the algorithm
distances, parents = dijkstra_sssp(my_graph, start_node, all_nodes)

# 4. Print the results
print("--- Dijkstra's Algorithm Results ---")
print(f"Source Node: {start_node}\n")
print("Shortest Path Distances to Target Destinations:")

most_likely_dist = float('inf')
most_likely_node = -1

for node in target_destinations:
    dist = distances[node]
    print(f"  - Node {node}: {dist}")
    if dist < most_likely_dist:
        most_likely_dist = dist
        most_likely_node = node

print("\n--- Conclusion ---")
print(f"The most likely destination is Node {most_likely_node} with a total path weight of {most_likely_dist}.")