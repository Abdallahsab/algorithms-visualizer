"""
Linear Search Algorithm
Time Complexity: O(n)
Space Complexity: O(1)
"""

def linear_search(arr, target, tracker=None):
    """
    Linear Search with performance tracking and step-by-step visualization
    Searches for target element sequentially through the array
    """
    for i, x in enumerate(arr):
        if tracker:
            tracker.comparisons += 1
            # Record current checking index
            if len(tracker.steps) < 50:  # Limit steps
                tracker.steps.append({'checking': i, 'found': False})
        
        if x == target:
            # Record found step
            if tracker and len(tracker.steps) < 50:
                tracker.steps.append({'checking': i, 'found': True})
            return i
    
    return -1
