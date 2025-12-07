"""
Quick Sort Algorithm
Time Complexity: O(n log n) average, O(n²) worst case
Space Complexity: O(log n)
Stable: No
"""

def quick_sort(arr, tracker=None):
    """
    Quick Sort with performance tracking
    Picks pivot element and partitions array around it
    """
    def _quick_sort(arr):
        if len(arr) <= 1:
            return arr
        
        pivot = arr[len(arr) // 2]
        left, mid, right = [], [], []
        
        for x in arr:
            if tracker:
                tracker.comparisons += 1
            
            if x < pivot:
                left.append(x)
            elif x == pivot:
                mid.append(x)
            else:
                right.append(x)
        
        result = _quick_sort(left) + mid + _quick_sort(right)
        
        if tracker and len(result) > 1 and len(tracker.steps) < 10:
            tracker.steps.append(result.copy())
        
        return result
    
    return _quick_sort(arr.copy())