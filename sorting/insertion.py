"""
Insertion Sort Algorithm
Time Complexity: O(n²)
Space Complexity: O(1)
Stable: Yes
"""

def insertion_sort(arr, tracker=None):
    """
    Insertion Sort with performance tracking and step-by-step visualization
    Builds sorted array one element at a time
    """
    arr = arr.copy()
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Record initial state of current key
        if tracker and len(tracker.steps) < 100:
            tracker.steps.append({
                'array': arr.copy(),
                'comparing': [i],
                'sorted': list(range(i))
            })
        
        while j >= 0:
            if tracker:
                tracker.comparisons += 1
            
            if arr[j] > key:
                arr[j + 1] = arr[j]
                if tracker:
                    tracker.swaps += 1
                    if len(tracker.steps) < 100:
                        tracker.steps.append({
                            'array': arr.copy(),
                            'comparing': [j, j+1],
                            'sorted': list(range(i))
                        })
                j -= 1
            else:
                break
        
        arr[j + 1] = key
        
        # Record state after insertion
        if tracker and len(tracker.steps) < 100:
            tracker.steps.append({
                'array': arr.copy(),
                'sorted': list(range(i+1))
            })
    
    # Final sorted state
    if tracker and len(tracker.steps) < 100:
        tracker.steps.append({
            'array': arr.copy(),
            'sorted': list(range(len(arr)))
        })
    
    return arr
