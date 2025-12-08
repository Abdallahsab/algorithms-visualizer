"""
Visual Representation for Algorithms
Handles drawing of sorting bars, search arrays, and graph structures
"""

import tkinter as tk
import math


class SortingVisualizer:
    """Visualize sorting algorithms with bars"""
    
    def __init__(self, canvas, width=800, height=300):
        self.canvas = canvas
        self.width = width
        self.height = height
        self.bars = []
        
    def draw_array(self, arr, highlighted=None, sorted_indices=None, swapped=None, comparing=None):
        """Draw array as vertical bars with multiple states"""
        self.canvas.delete("all")
        
        if not arr:
            return
        
        n = len(arr)
        max_val = max(arr) if arr else 1
        bar_width = (self.width - 40) / n
        
        for i, val in enumerate(arr):
            x0 = 20 + i * bar_width
            y0 = self.height - 20
            x1 = x0 + bar_width - 2
            y1 = y0 - (val / max_val) * (self.height - 60)
            
            # Determine color based on state
            if sorted_indices and i in sorted_indices:
                color = "#2ecc71"  # Green for sorted
                outline = "white"
                width = 2
            elif swapped and i in swapped:
                color = "#e74c3c"  # Red for just swapped
                outline = "white"
                width = 3
            elif comparing and i in comparing:
                color = "#f39c12"  # Orange for comparing
                outline = "white"
                width = 3
            elif highlighted and i in highlighted:
                color = "#9b59b6"  # Purple for highlighted
                outline = "white"
                width = 2
            else:
                color = "#3498db"  # Blue default (unsorted)
                outline = "#5dade2"
                width = 1
            
            # Draw bar
            self.canvas.create_rectangle(x0, y0, x1, y1, 
                                        fill=color, outline=outline, width=width)
            
            # Draw value
            font_size = 8 if n > 15 else 10
            self.canvas.create_text((x0 + x1) / 2, y1 - 10,
                                   text=str(val), fill="white", 
                                   font=("Arial", font_size, "bold"))
        
        # Draw legend
        self._draw_sorting_legend()
    
    def _draw_sorting_legend(self):
        """Draw legend for sorting visualization"""
        legend_y = self.height - 30
        items = [
            ("#3498db", "Unsorted"),
            ("#f39c12", "Comparing"),
            ("#e74c3c", "Swapped"),
            ("#2ecc71", "Sorted")
        ]
        
        x = 20
        for color, label in items:
            self.canvas.create_rectangle(x, legend_y, x + 15, legend_y + 15,
                                        fill=color, outline="white")
            self.canvas.create_text(x + 25, legend_y + 7, text=label,
                                   fill="white", font=("Arial", 9),
                                   anchor="w")
            x += 110


class SearchVisualizer:
    """Visualize search algorithms"""
    
    def __init__(self, canvas, width=800, height=150):
        self.canvas = canvas
        self.width = width
        self.height = height
        
    def draw_array(self, arr, target=None, found_index=None, checking_index=None, 
                   binary_left=None, binary_right=None, binary_mid=None):
        """Draw array as boxes with search visualization"""
        self.canvas.delete("all")
        
        if not arr:
            return
        
        n = len(arr)
        box_width = min(60, (self.width - 40) / n)
        start_x = (self.width - (box_width * n)) / 2
        
        for i, val in enumerate(arr):
            x0 = start_x + i * box_width
            y0 = 50
            x1 = x0 + box_width - 5
            y1 = y0 + 50
            
            # Determine color based on search type
            if found_index is not None and i == found_index:
                color = "#2ecc71"  # Green for found
                outline = "white"
                width = 3
            elif binary_mid is not None and i == binary_mid:
                color = "#f39c12"  # Orange for binary mid
                outline = "white"
                width = 3
            elif checking_index is not None and i == checking_index:
                color = "#f39c12"  # Orange for linear checking
                outline = "white"
                width = 3
            elif binary_left is not None and binary_right is not None:
                if binary_left <= i <= binary_right:
                    color = "#3498db"  # Blue for binary search range
                    outline = "#5dade2"
                    width = 2
                else:
                    color = "#34495e"  # Gray for out of range
                    outline = "#7f8c8d"
                    width = 1
            else:
                color = "#34495e"  # Gray default
                outline = "#7f8c8d"
                width = 1
            
            # Draw box
            self.canvas.create_rectangle(x0, y0, x1, y1, 
                                        fill=color, outline=outline, width=width)
            
            # Draw value
            self.canvas.create_text((x0 + x1) / 2, (y0 + y1) / 2,
                                   text=str(val), fill="white", 
                                   font=("Arial", 12, "bold"))
            
            # Draw index
            self.canvas.create_text((x0 + x1) / 2, y1 + 15,
                                   text=f"[{i}]", fill="#95a5a6", 
                                   font=("Arial", 8))
            
            # Mark left, right, mid for binary search
            if binary_left is not None and i == binary_left:
                self.canvas.create_text((x0 + x1) / 2, y0 - 15,
                                       text="L", fill="#3498db", 
                                       font=("Arial", 10, "bold"))
            if binary_right is not None and i == binary_right:
                self.canvas.create_text((x0 + x1) / 2, y0 - 15,
                                       text="R", fill="#3498db", 
                                       font=("Arial", 10, "bold"))
            if binary_mid is not None and i == binary_mid:
                self.canvas.create_text((x0 + x1) / 2, y0 - 15,
                                       text="M", fill="#f39c12", 
                                       font=("Arial", 10, "bold"))
        
        # Draw target indicator
        if target is not None:
            self.canvas.create_text(self.width / 2, 20,
                                   text=f"🎯 Target: {target}", 
                                   fill="#e74c3c", 
                                   font=("Arial", 14, "bold"))
        
        # Draw legend
        self._draw_search_legend(binary_left is not None)
    
    def _draw_search_legend(self, is_binary=False):
        """Draw legend for search visualization"""
        legend_y = self.height - 20
        
        if is_binary:
            items = [
                ("#3498db", "Search Range"),
                ("#f39c12", "Checking (Mid)"),
                ("#2ecc71", "Found"),
                ("#34495e", "Excluded")
            ]
        else:
            items = [
                ("#f39c12", "Checking"),
                ("#2ecc71", "Found"),
                ("#34495e", "Not Checked")
            ]
        
        x = 20
        for color, label in items:
            self.canvas.create_rectangle(x, legend_y, x + 15, legend_y + 15,
                                        fill=color, outline="white")
            self.canvas.create_text(x + 25, legend_y + 7, text=label,
                                   fill="white", font=("Arial", 8),
                                   anchor="w")
            x += 120


class GraphVisualizer:
    """Visualize graph traversal"""
    
    def __init__(self, canvas, width=800, height=400):
        self.canvas = canvas
        self.width = width
        self.height = height
        self.node_positions = {}
        
    def calculate_positions(self, graph, start):
        """Calculate node positions for tree-like layout"""
        self.node_positions = {}
        visited = set()
        levels = {}
        
        # BFS to assign levels
        queue = [(start, 0)]
        visited.add(start)
        max_level = 0
        
        while queue:
            node, level = queue.pop(0)
            if level not in levels:
                levels[level] = []
            levels[level].append(node)
            max_level = max(max_level, level)
            
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, level + 1))
        
        # Calculate positions
        for level, nodes in levels.items():
            y = 60 + level * 80
            total_width = len(nodes) * 100
            start_x = (self.width - total_width) / 2 + 50
            
            for i, node in enumerate(nodes):
                x = start_x + i * 100
                self.node_positions[node] = (x, y)
        
        return self.node_positions
    
    def draw_graph(self, graph, start, visited_order=None, current_node=None):
        """Draw graph with nodes and edges"""
        self.canvas.delete("all")
        
        if not graph:
            return
        
        # Calculate positions if not done
        if not self.node_positions:
            self.calculate_positions(graph, start)
        
        # Draw edges first (so they appear behind nodes)
        for node, neighbors in graph.items():
            if node in self.node_positions:
                x1, y1 = self.node_positions[node]
                for neighbor in neighbors:
                    if neighbor in self.node_positions:
                        x2, y2 = self.node_positions[neighbor]
                        
                        # Color edge if both nodes visited
                        if visited_order and node in visited_order and neighbor in visited_order:
                            color = "#3498db"
                            width = 2
                        else:
                            color = "#7f8c8d"
                            width = 1
                        
                        # Draw arrow
                        self.canvas.create_line(x1, y1, x2, y2, 
                                              fill=color, width=width, 
                                              arrow=tk.LAST, arrowshape=(10, 12, 5))
        
        # Draw nodes
        for node, (x, y) in self.node_positions.items():
            # Determine color
            if current_node and node == current_node:
                color = "#f39c12"  # Orange for current
                outline = "white"
                width = 4
            elif visited_order and node in visited_order:
                # Gradient based on visit order
                idx = visited_order.index(node)
                color = "#2ecc71"  # Green for visited
                outline = "white"
                width = 2
            elif node == start:
                color = "#e74c3c"  # Red for start
                outline = "white"
                width = 3
            else:
                color = "#34495e"  # Gray for unvisited
                outline = "#7f8c8d"
                width = 1
            
            # Draw circle
            r = 25
            self.canvas.create_oval(x - r, y - r, x + r, y + r,
                                   fill=color, outline=outline, width=width)
            
            # Draw node label
            self.canvas.create_text(x, y, text=str(node),
                                   fill="white", font=("Arial", 14, "bold"))
            
            # Draw visit order
            if visited_order and node in visited_order:
                order = visited_order.index(node) + 1
                self.canvas.create_text(x + r + 10, y - r - 10,
                                       text=f"#{order}", fill="#2ecc71",
                                       font=("Arial", 10, "bold"))
        
        # Draw legend
        self._draw_legend()
    
    def _draw_legend(self):
        """Draw legend for graph colors"""
        legend_y = self.height - 30
        items = [
            ("#e74c3c", "Start"),
            ("#f39c12", "Current"),
            ("#2ecc71", "Visited"),
            ("#34495e", "Unvisited")
        ]
        
        x = 20
        for color, label in items:
            # Draw circle
            self.canvas.create_oval(x, legend_y, x + 15, legend_y + 15,
                                   fill=color, outline="white")
            # Draw label
            self.canvas.create_text(x + 25, legend_y + 7, text=label,
                                   fill="white", font=("Arial", 9),
                                   anchor="w")
            x += 100