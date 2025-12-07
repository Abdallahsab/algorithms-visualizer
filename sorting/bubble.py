"""
Bubble Sort Algorithm
Time Complexity: O(n²)
Space Complexity: O(1)
Stable: Yes
"""

def bubble_sort(arr, tracker=None):
    """
    Bubble Sort with performance tracking
    Repeatedly swaps adjacent elements if they're in wrong order
    """
    n = len(arr)
    arr = arr.copy()
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if tracker:
                tracker.comparisons += 1
            
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                if tracker:
                    tracker.swaps += 1
                    if len(tracker.steps) < 10:
                        tracker.steps.append(arr.copy())
    
    return arr