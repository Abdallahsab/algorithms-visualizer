"""
Selection Sort Algorithm
Time Complexity: O(n²)
Space Complexity: O(1)
Stable: No
"""

def selection_sort(arr, tracker=None):
    """
    Selection Sort with performance tracking and step-by-step visualization
    Selects minimum element and places it at beginning
    """
    arr = arr.copy()
    
    for i in range(len(arr)):
        min_idx = i
        
        for j in range(i + 1, len(arr)):
            if tracker:
                tracker.comparisons += 1
                # Record comparing state
                if len(tracker.steps) < 100:
                    tracker.steps.append({
                        'array': arr.copy(),
                        'comparing': [min_idx, j],
                        'sorted': list(range(i))
                    })
            
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            if tracker:
                tracker.swaps += 1
                # Record swapped state
                if len(tracker.steps) < 100:
                    tracker.steps.append({
                        'array': arr.copy(),
                        'swapped': [i, min_idx],
                        'sorted': list(range(i+1))
                    })
    
    # Final sorted state
    if tracker and len(tracker.steps) < 100:
        tracker.steps.append({
            'array': arr.copy(),
            'sorted': list(range(len(arr)))
        })
    
    return arr
