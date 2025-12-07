"""
Linear Search Algorithm
Time Complexity: O(n)
Space Complexity: O(1)
"""

def linear_search(arr, target, tracker=None):
    """
    Linear Search with performance tracking
    Searches for target element sequentially through the array
    """
    for i, x in enumerate(arr):
        if tracker:
            tracker.comparisons += 1
        
        if x == target:
            return i
    
    return -1