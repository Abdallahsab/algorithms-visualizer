"""
Depth-First Search (DFS) Algorithm
Time Complexity: O(V + E)
Space Complexity: O(V)
"""

def dfs(graph, start, tracker=None):
    """
    DFS with performance tracking and step-by-step visualization
    Explores as deep as possible before backtracking
    """
    visited = []
    stack = [start]
    seen = set([start])
    
    while stack:
        node = stack.pop()
        visited.append(node)
        
        # Record step with current node being processed
        if tracker and len(tracker.steps) < 50:
            tracker.steps.append({
                'visited': visited.copy(),
                'current': node,
                'stack': stack.copy()
            })
        
        for neighbor in reversed(graph.get(node, [])):
            if tracker:
                tracker.comparisons += 1
            
            if neighbor not in seen:
                seen.add(neighbor)
                stack.append(neighbor)
    
    return visited
