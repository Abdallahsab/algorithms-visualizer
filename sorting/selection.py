"""
Selection Sort Algorithm
Time Complexity: O(n²)
Space Complexity: O(1)
Stable: No
"""

def selection_sort(arr, tracker=None):
    """
    Selection Sort with performance tracking
    Selects minimum element and places it at beginning
    """
    arr = arr.copy()
    
    for i in range(len(arr)):
        min_idx = i
        
        for j in range(i + 1, len(arr)):
            if tracker:
                tracker.comparisons += 1
            
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        if tracker:
            tracker.swaps += 1
            if len(tracker.steps) < 10:
                tracker.steps.append(arr.copy())
    
    return arr