"""
Merge Sort Algorithm
Time Complexity: O(n log n)
Space Complexity: O(n)
Stable: Yes
"""

def merge_sort(arr, tracker=None):
    """
    Merge Sort with performance tracking
    Divide and conquer algorithm that splits array and merges sorted halves
    """
    def _merge_sort(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            L, R = arr[:mid], arr[mid:]
            
            _merge_sort(L)
            _merge_sort(R)
            
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
            
            if tracker and len(tracker.steps) < 10:
                tracker.steps.append(arr.copy())
        
        return arr
    
    arr = arr.copy()
    return _merge_sort(arr)