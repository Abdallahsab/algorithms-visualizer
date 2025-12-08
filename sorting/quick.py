"""
Quick Sort Algorithm
Time Complexity: O(n log n) average, O(n²) worst case
Space Complexity: O(log n)
Stable: No
"""

def quick_sort(arr, tracker=None):
    """
    Quick Sort with performance tracking and step-by-step visualization
    Picks pivot element and partitions array around it
    """
    def _quick_sort(arr, low, high):
        if low < high:
            # Partition and get pivot index
            pivot_idx = partition(arr, low, high)
            
            # Record partitioned state
            if tracker and len(tracker.steps) < 100:
                tracker.steps.append({
                    'array': arr.copy(),
                    'comparing': [pivot_idx],
                    'sorted': []
                })
            
            # Recursively sort elements
            _quick_sort(arr, low, pivot_idx - 1)
            _quick_sort(arr, pivot_idx + 1, high)
    
    def partition(arr, low, high):
        # Choose the rightmost element as pivot
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            if tracker:
                tracker.comparisons += 1
                # Record comparing state
                if len(tracker.steps) < 100:
                    tracker.steps.append({
                        'array': arr.copy(),
                        'comparing': [j, high],
                        'sorted': []
                    })
            
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                
                if tracker and i != j:
                    tracker.swaps += 1
                    # Record swapped state
                    if len(tracker.steps) < 100:
                        tracker.steps.append({
                            'array': arr.copy(),
                            'swapped': [i, j],
                            'sorted': []
                        })
        
        # Place pivot in correct position
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        
        if tracker:
            tracker.swaps += 1
            if len(tracker.steps) < 100:
                tracker.steps.append({
                    'array': arr.copy(),
                    'swapped': [i + 1, high],
                    'sorted': []
                })
        
        return i + 1
    
    arr = arr.copy()
    _quick_sort(arr, 0, len(arr) - 1)
    
    # Final sorted state
    if tracker and len(tracker.steps) < 100:
        tracker.steps.append({
            'array': arr.copy(),
            'sorted': list(range(len(arr)))
        })
    
    return arr
