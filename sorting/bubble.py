"""
Bubble Sort Algorithm
Time Complexity: O(n²)
Space Complexity: O(1)
Stable: Yes
"""

def bubble_sort(arr, tracker=None):
    """
    Bubble Sort with performance tracking and step-by-step visualization
    Repeatedly swaps adjacent elements if they're in wrong order
    """
    n = len(arr)
    arr = arr.copy()
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if tracker:
                tracker.comparisons += 1
                # Record comparing state
                if len(tracker.steps) < 100:
                    tracker.steps.append({
                        'array': arr.copy(),
                        'comparing': [j, j+1],
                        'sorted': list(range(n-i, n))
                    })
            
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                if tracker:
                    tracker.swaps += 1
                    # Record swapped state
                    if len(tracker.steps) < 100:
                        tracker.steps.append({
                            'array': arr.copy(),
                            'swapped': [j, j+1],
                            'sorted': list(range(n-i, n))
                        })
    
    # Final sorted state
    if tracker and len(tracker.steps) < 100:
        tracker.steps.append({
            'array': arr.copy(),
            'sorted': list(range(n))
        })
    
    return arr
