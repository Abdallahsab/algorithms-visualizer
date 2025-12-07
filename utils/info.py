"""
Algorithm Information and Complexity Details
"""

ALGO_INFO = {
    "Bubble Sort": "Time: O(n²) | Space: O(1) | Stable: Yes\nSimple comparison sort, best for small datasets",
    "Insertion Sort": "Time: O(n²) | Space: O(1) | Stable: Yes\nEfficient for small or nearly sorted data",
    "Selection Sort": "Time: O(n²) | Space: O(1) | Stable: No\nMinimizes number of swaps",
    "Merge Sort": "Time: O(n log n) | Space: O(n) | Stable: Yes\nGuaranteed O(n log n), good for large datasets",
    "Quick Sort": "Time: O(n log n) avg | Space: O(log n) | Stable: No\nFast in practice, cache-efficient",
    "Linear Search": "Time: O(n) | Space: O(1)\nSearches sequentially through array",
    "Binary Search": "Time: O(log n) | Space: O(1)\nRequires sorted array, very efficient",
    "BFS": "Time: O(V+E) | Space: O(V)\nLevel-order traversal, finds shortest path",
    "DFS": "Time: O(V+E) | Space: O(V)\nDepth-first exploration, uses less memory",
}