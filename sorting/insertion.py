"""
Insertion Sort Algorithm
Time Complexity: O(n²)
Space Complexity: O(1)
Stable: Yes
"""

def insertion_sort(arr, tracker=None):
    """
    Insertion Sort with performance tracking
    Builds sorted array one element at a time
    """
    arr = arr.copy()
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0:
            if tracker:
                tracker.comparisons += 1
            
            if arr[j] > key:
                arr[j + 1] = arr[j]
                if tracker:
                    tracker.swaps += 1
                j -= 1
            else:
                break
        
        arr[j + 1] = key
        if tracker and len(tracker.steps) < 10:
            tracker.steps.append(arr.copy())
    
    return arr