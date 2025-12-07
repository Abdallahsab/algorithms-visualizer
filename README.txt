 🔢 Algorithms Visualizer 

A comprehensive and professional algorithm visualization tool built with Python and ttkbootstrap. Perfect for learning, teaching, and analyzing fundamental computer science algorithms.
---

✨ Features
 🔄 **5 Sorting Algorithms**
- **Bubble Sort** - O(n²) time complexity
- **Insertion Sort** - O(n²) time complexity
- **Selection Sort** - O(n²) time complexity
- **Merge Sort** - O(n log n) time complexity
- **Quick Sort** - O(n log n) average time complexity

 🔍 **2 Search Algorithms**
- **Linear Search** - O(n) time complexity
- **Binary Search** - O(log n) time complexity

 🕸️ **2 Graph Traversal Algorithms**
- **BFS (Breadth-First Search)** - Level-order traversal
- **DFS (Depth-First Search)** - Depth-first exploration

 📊 **Performance Metrics**
- Real-time execution time measurement
- Comparison count tracking
- Swap/operation count tracking
- Step-by-step visualization

 🎨 **Modern User Interface**
- Professional dark theme
- Intuitive tabbed interface
- Pre-loaded example datasets
- Export results functionality
- Algorithm complexity information

---

💻 Usage

 Sorting Algorithms

1. Navigate to the **"🔢 Sorting"** tab
2. Enter numbers separated by commas (e.g., `64, 34, 25, 12, 22, 11, 90`)
3. Select an algorithm from the dropdown
4. Click **"▶ Run"** to execute
5. View detailed performance metrics and results

**Example Input:**
```
64, 34, 25, 12, 22, 11, 90
```

**Example Output:**
```
Original: [64, 34, 25, 12, 22, 11, 90]
Sorted:   [11, 12, 22, 25, 34, 64, 90]

Performance Metrics:
⏱ Time:         0.0234 ms
🔄 Comparisons:  21
↔ Swaps:         12
```

 Search Algorithms

1. Navigate to the **"🔍 Searching"** tab
2. Enter array elements (e.g., `10, 20, 30, 40, 50`)
3. Enter target value to search for
4. Select search algorithm
5. Click **"▶ Run"** to execute

 Graph Traversal

1. Navigate to the **"🕸 Graph Traversal"** tab
2. Enter graph definition (format: `A:B,C B:D,E C:F`)
3. Enter starting node
4. Select BFS or DFS
5. Click **"▶ Run"** to execute

---

## 📊 Performance Comparison

| Algorithm | Time Complexity | Space Complexity | Stable |
|-----------|----------------|------------------|--------|
| Bubble Sort | O(n²) | O(1) | Yes |
| Insertion Sort | O(n²) | O(1) | Yes |
| Selection Sort | O(n²) | O(1) | No |
| Merge Sort | O(n log n) | O(n) | Yes |
| Quick Sort | O(n log n) avg | O(log n) | No |
| Linear Search | O(n) | O(1) | - |
| Binary Search | O(log n) | O(1) | - |
| BFS | O(V + E) | O(V) | - |
| DFS | O(V + E) | O(V) | - |

---

 📝 Example Datasets

The application includes pre-loaded examples:

  Sorting Examples:
- Random Small: `64, 34, 25, 12, 22, 11, 90`
- Random Medium: `45, 23, 78, 12, 90, 34, 67, 89, 15, 56`
- Nearly Sorted: `10, 20, 15, 30, 25, 40, 35, 50`
- Reverse Order: `100, 90, 80, 70, 60, 50, 40, 30`

 Search Examples:
- Simple List: Array: `10, 20, 30, 40, 50, 60, 70, 80`, Target: `50`
- Large List: Array: `5, 15, 25, 35, 45, 55, 65, 75, 85, 95`, Target: `65`

 Graph Examples:
- Simple Tree: `A:B,C B:D,E C:F,G`, Start: `A`
- Connected Graph: `A:B,C B:D C:D,E D:E,F`, Start: `A`
- Complex Graph: `A:B,C,D B:E,F C:G D:H E:I F:J G:K H:L`, Start: `A`

---

 🎯 Features in Detail

 Performance Tracking
- **Comparisons**: Number of element comparisons performed
- **Swaps**: Number of element swaps or movements
- **Execution Time**: Actual time taken in milliseconds
- **Step-by-step**: Visual representation of algorithm progress

 Export Functionality
- Export results to text file
- Includes all performance metrics
- Timestamp for each export
- Accessible via File → Export Results

 Algorithm Information
- Time complexity display
- Space complexity display
- Stability information
- Best use cases for each algorithm

---

🔮 Future Enhancements

- [ ] Add more sorting algorithms (Heap Sort, Radix Sort)
- [ ] Animated visualization of sorting steps
- [ ] Algorithm comparison mode
- [ ] Custom theme support
- [ ] Save/load custom test cases
- [ ] More graph algorithms (Dijkstra, A*)
- [ ] Performance benchmarking suite

---

