"""
Breadth-First Search (BFS) Algorithm
Time Complexity: O(V + E)
Space Complexity: O(V)
"""

from collections import deque

def bfs(graph, start, tracker=None):
    """
    BFS with performance tracking
    Explores graph level by level, finds shortest path in unweighted graphs
    """
    visited = []
    queue = deque([start])
    seen = set([start])
    
    while queue:
        node = queue.popleft()
        visited.append(node)
        
        if tracker and len(tracker.steps) < 20:
            tracker.steps.append(visited.copy())
        
        for neighbor in graph.get(node, []):
            if tracker:
                tracker.comparisons += 1
            
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)
    
    return visited