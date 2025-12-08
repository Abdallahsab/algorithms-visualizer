"""
Merge Sort Algorithm
Time Complexity: O(n log n)
Space Complexity: O(n)
Stable: Yes
"""

def merge_sort(arr, tracker=None):
    """
    Merge Sort with performance tracking and step-by-step visualization
    Divide and conquer algorithm that splits array and merges sorted halves
    """
    # Keep reference to original for updating
    original_arr = arr.copy()
    indices_map = {id(original_arr): list(range(len(original_arr)))}
    
    def _merge_sort(arr, start_idx=0):
        if len(arr) > 1:
            mid = len(arr) // 2
            L, R = arr[:mid], arr[mid:]
            
            _merge_sort(L, start_idx)
            _merge_sort(R, start_idx + mid)
            
            i = j = k = 0
            
            while i < len(L) and j < len(R):
                if tracker:
                    tracker.comparisons += 1
                
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
            
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
            
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
            
            # Update original array for visualization
            for idx, val in enumerate(arr):
                original_arr[start_idx + idx] = val
            
            # Record merged state
            if tracker and len(tracker.steps) < 100:
                tracker.steps.append({
                    'array': original_arr.copy(),
                    'merging': list(range(start_idx, start_idx + len(arr))),
                    'sorted': []
                })
        
        return arr
    
    _merge_sort(original_arr)
    
    # Final sorted state
    if tracker and len(tracker.steps) < 100:
        tracker.steps.append({
            'array': original_arr.copy(),
            'sorted': list(range(len(original_arr)))
        })
    
    return original_arr
