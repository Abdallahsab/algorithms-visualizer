"""
Binary Search Algorithm
Time Complexity: O(log n)
Space Complexity: O(1)
"""

def binary_search(arr, target, tracker=None):
    """
    Binary Search with performance tracking and step-by-step visualization
    Requires sorted array. Divides search space in half each iteration.
    """
    arr = sorted(arr)
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if tracker:
            tracker.comparisons += 1
            # Record current checking range and mid
            if len(tracker.steps) < 50:
                tracker.steps.append({
                    'left': left,
                    'right': right,
                    'mid': mid,
                    'found': False
                })
        
        if arr[mid] == target:
            # Record found step
            if tracker and len(tracker.steps) < 50:
                tracker.steps.append({
                    'left': left,
                    'right': right,
                    'mid': mid,
                    'found': True
                })
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1
