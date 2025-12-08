"""
Algorithms Visualizer Pro - Main GUI with Complete Animation
"""

import sys
import os

# Add parent directory to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import ttkbootstrap as tb
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import Messagebox
import tkinter as tk
import time

# Import algorithms
from sorting.bubble import bubble_sort
from sorting.insertion import insertion_sort
from sorting.selection import selection_sort
from sorting.merge import merge_sort
from sorting.quick import quick_sort
from searching.linear_search import linear_search
from searching.binary_search import binary_search
from traversal.graph_bfs import bfs as graph_bfs
from traversal.graph_dfs import dfs as graph_dfs

# Import utilities
from utils import (AlgorithmTracker, EXAMPLES, ALGO_INFO, 
                   SortingVisualizer, SearchVisualizer, GraphVisualizer)


def parse_graph(text):
    """Parse graph string into dictionary"""
    items = text.replace(";", " ").split()
    graph = {}
    for p in items:
        if ":" not in p:
            raise ValueError("Invalid: " + p)
        node, nbrs = p.split(":", 1)
        graph[node.strip()] = [n.strip() for n in nbrs.split(",") if n.strip()]
    return graph


def create_app():
    app = tb.Window(themename="darkly")
    app.title("Algorithms Visualizer Pro - Animated Edition")
    app.geometry("1200x850")
    app.minsize(1000, 700)

    last_results = {"sort": "", "search": "", "graph": ""}

    def export_results():
        if not any(last_results.values()):
            Messagebox.show_info("No Results", "Run an algorithm first.")
            return
        try:
            with open("algorithm_results.txt", "w", encoding="utf-8") as f:
                f.write("="*60 + "\nALGORITHM RESULTS EXPORT\n" + "="*60 + "\n\n")
                for cat, res in last_results.items():
                    if res:
                        f.write(f"\n{'='*20} {cat.upper()} {'='*20}\n{res}\n")
                f.write(f"\n{'='*60}\nExported: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            Messagebox.show_info("Success", "Exported to 'algorithm_results.txt'")
        except Exception as e:
            Messagebox.show_error("Export Error", str(e))

    def show_about():
        Messagebox.show_info("About", "Algorithms Visualizer Pro v2.0\n\nAnimated Edition\n\nFeatures:\n• 5 Sorting Algorithms with animation\n• 2 Search Algorithms with step-by-step\n• 2 Graph Traversal with visual tree\n• Real-time performance tracking")

    menubar = tb.Menu(app)
    app.config(menu=menubar)
    file_menu = tb.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Export Results", command=export_results)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=app.quit)
    help_menu = tb.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(label="About", command=show_about)

    nb = tb.Notebook(app)
    nb.pack(fill="both", expand=True, padx=10, pady=10)

    # ============================================================
    # SORTING TAB
    # ============================================================
    tab_sort = tb.Frame(nb)
    nb.add(tab_sort, text="🔢 Sorting")
    
    top_frame_sort = tb.Frame(tab_sort)
    top_frame_sort.pack(fill="x", padx=10, pady=10)
    
    card_sort = tb.Labelframe(top_frame_sort, text="Sorting Controls", padding=10, bootstyle="primary")
    card_sort.pack(fill="x")

    tb.Label(card_sort, text="Numbers (comma separated):").pack(anchor="w", padx=5, pady=2)
    entry_sort = tb.Entry(card_sort, width=70, font=("Inter", 10))
    entry_sort.pack(fill="x", padx=5, pady=3)

    ex_frame = tb.Frame(card_sort)
    ex_frame.pack(fill="x", padx=5, pady=3)
    tb.Label(ex_frame, text="Example:").pack(side="left", padx=(0,5))
    ex_var = tb.StringVar(value="Select...")
    ex_combo = tb.Combobox(ex_frame, textvariable=ex_var, values=list(EXAMPLES["sort"].keys()), width=18, state="readonly")
    ex_combo.pack(side="left")
    
    def load_ex(e=None):
        if ex_var.get() in EXAMPLES["sort"]:
            entry_sort.delete(0,'end')
            entry_sort.insert(0, EXAMPLES["sort"][ex_var.get()])
            try:
                arr = [int(x.strip()) for x in entry_sort.get().split(",") if x.strip()]
                sort_viz.draw_array(arr)
            except:
                pass
    ex_combo.bind("<<ComboboxSelected>>", load_ex)

    algo_frame = tb.Frame(card_sort)
    algo_frame.pack(fill="x", padx=5, pady=5)
    tb.Label(algo_frame, text="Algorithm:").pack(side="left", padx=(0,5))
    sort_algos = ["Bubble Sort","Insertion Sort","Selection Sort","Merge Sort","Quick Sort"]
    sel_sort = tb.StringVar(value=sort_algos[0])
    combo_sort = tb.Combobox(algo_frame, values=sort_algos, textvariable=sel_sort, width=20, state="readonly")
    combo_sort.pack(side="left", padx=(0,10))
    info_lbl = tb.Label(algo_frame, text="", font=("Inter",9), foreground="gray")
    info_lbl.pack(side="left", fill="x", expand=True)
    
    def update_info(e=None):
        info_lbl.config(text=ALGO_INFO.get(sel_sort.get(),""))
    combo_sort.bind("<<ComboboxSelected>>", update_info)
    update_info()

    btn_frame = tb.Frame(card_sort)
    btn_frame.pack(pady=8, padx=5)
    run_btn = tb.Button(btn_frame, text="▶ Run & Visualize", bootstyle=SUCCESS, width=15)
    run_btn.pack(side="left", padx=5)
    clear_btn = tb.Button(btn_frame, text="🗑 Clear", bootstyle=DANGER, width=10)
    clear_btn.pack(side="left", padx=5)

    viz_frame_sort = tb.Labelframe(tab_sort, text="🎨 Visual Representation", padding=10, bootstyle="info")
    viz_frame_sort.pack(fill="both", expand=True, padx=10, pady=5)
    
    canvas_sort = tk.Canvas(viz_frame_sort, bg="#2c3e50", height=300, highlightthickness=0)
    canvas_sort.pack(fill="both", expand=True, padx=5, pady=5)
    sort_viz = SortingVisualizer(canvas_sort, width=1100, height=300)

    metrics_frame = tb.Labelframe(tab_sort, text="Performance Metrics", padding=5, bootstyle="success")
    metrics_frame.pack(fill="x", padx=10, pady=5)
    met_display = tb.Frame(metrics_frame)
    met_display.pack(fill="x")
    metric_labels = {}
    for i, (key, lbl) in enumerate([("time","⏱ Time:"),("comp","🔄 Comparisons:"),("swap","↔ Swaps:")]):
        tb.Label(met_display, text=lbl, font=("Inter",9,"bold")).grid(row=0, column=i*2, sticky="w", padx=(0,5))
        metric_labels[key] = tb.Label(met_display, text="—", font=("Inter",9), foreground="cyan")
        metric_labels[key].grid(row=0, column=i*2+1, sticky="w", padx=(0,15))

    tb.Label(tab_sort, text="Output:", font=("Inter",10,"bold")).pack(anchor="w", padx=15, pady=(5,2))
    out_frame = tb.Frame(tab_sort, relief="solid", borderwidth=1)
    out_frame.pack(fill="x", padx=10, pady=5)
    output_sort = tb.Text(out_frame, wrap="word", height=4, font=("Consolas",10), bd=0)
    output_sort.pack(side="left", fill="both", expand=True)
    scroll_sort = tb.Scrollbar(out_frame, command=output_sort.yview)
    output_sort.configure(yscrollcommand=scroll_sort.set)
    scroll_sort.pack(side="right", fill="y")

    def run_sort():
        output_sort.delete("1.0","end")
        try:
            arr = [int(x.strip()) for x in entry_sort.get().split(",") if x.strip()]
            if not arr: raise ValueError()
        except:
            Messagebox.show_error("Input Error", "Enter valid integers.")
            return
        
        sort_viz.draw_array(arr)
        app.update()
        time.sleep(0.3)
        
        tracker = AlgorithmTracker()
        algo_map = {"Bubble Sort": bubble_sort, "Insertion Sort": insertion_sort, 
                    "Selection Sort": selection_sort, "Merge Sort": merge_sort, 
                    "Quick Sort": quick_sort}
        
        start = time.perf_counter()
        result = algo_map[sel_sort.get()](arr, tracker)
        end = time.perf_counter()
        tracker.time_taken = (end - start) * 1000
        
        if tracker.steps:
            for step_data in tracker.steps:
                current_arr = step_data.get('array')
                comparing = step_data.get('comparing', [])
                swapped = step_data.get('swapped', [])
                sorted_idx = step_data.get('sorted', [])
                merging = step_data.get('merging', [])
                
                sort_viz.draw_array(current_arr, 
                                   comparing=comparing,
                                   swapped=swapped,
                                   sorted_indices=sorted_idx,
                                   highlighted=merging)
                app.update()
                
                delay = 0.05 if len(arr) > 20 else 0.2
                time.sleep(delay)
        else:
            sort_viz.draw_array(result, sorted_indices=list(range(len(result))))
        
        metric_labels["time"].config(text=f"{tracker.time_taken:.3f} ms")
        metric_labels["comp"].config(text=str(tracker.comparisons))
        metric_labels["swap"].config(text=str(tracker.swaps))
        
        output_sort.insert("end", f"Original: {arr}\n", "bold")
        output_sort.insert("end", f"Sorted: {result}\n", "result")
        output_sort.insert("end", f"✓ {sel_sort.get()} | Size: {len(arr)} | Comp: {tracker.comparisons} | Swaps: {tracker.swaps} | Time: {tracker.time_taken:.3f}ms", "success")
        output_sort.tag_config("bold", font=("Consolas",10,"bold"))
        output_sort.tag_config("result", foreground="lightgreen", font=("Consolas",10,"bold"))
        output_sort.tag_config("success", foreground="lightgreen")
        
        last_results["sort"] = f"{sel_sort.get()}\nInput: {arr}\nOutput: {result}\nTime: {tracker.time_taken:.3f}ms"

    def clear_sort():
        entry_sort.delete(0,'end')
        output_sort.delete("1.0","end")
        canvas_sort.delete("all")
        for lbl in metric_labels.values(): lbl.config(text="—")

    run_btn.configure(command=run_sort)
    clear_btn.configure(command=clear_sort)

    # ============================================================
    # SEARCHING TAB
    # ============================================================
    tab_search = tb.Frame(nb)
    nb.add(tab_search, text="🔍 Searching")
    
    top_frame_search = tb.Frame(tab_search)
    top_frame_search.pack(fill="x", padx=10, pady=10)
    
    card_search = tb.Labelframe(top_frame_search, text="Search Controls", padding=10, bootstyle="primary")
    card_search.pack(fill="x")

    tb.Label(card_search, text="Numbers (comma separated):").pack(anchor="w", padx=5, pady=2)
    entry_search = tb.Entry(card_search, width=70, font=("Inter",10))
    entry_search.pack(fill="x", padx=5, pady=3)
    tb.Label(card_search, text="Target Value:").pack(anchor="w", padx=5, pady=2)
    entry_target = tb.Entry(card_search, width=20, font=("Inter",10))
    entry_target.pack(anchor="w", padx=5, pady=3)

    ex_frame_s = tb.Frame(card_search)
    ex_frame_s.pack(fill="x", padx=5, pady=3)
    tb.Label(ex_frame_s, text="Example:").pack(side="left", padx=(0,5))
    ex_var_s = tb.StringVar(value="Select...")
    ex_combo_s = tb.Combobox(ex_frame_s, textvariable=ex_var_s, values=list(EXAMPLES["search"].keys()), width=18, state="readonly")
    ex_combo_s.pack(side="left")
    
    def load_ex_s(e=None):
        if ex_var_s.get() in EXAMPLES["search"]:
            data, tgt = EXAMPLES["search"][ex_var_s.get()]
            entry_search.delete(0,'end')
            entry_search.insert(0, data)
            entry_target.delete(0,'end')
            entry_target.insert(0, tgt)
            try:
                arr = [int(x.strip()) for x in data.split(",") if x.strip()]
                search_viz.draw_array(arr, target=int(tgt))
            except:
                pass
    ex_combo_s.bind("<<ComboboxSelected>>", load_ex_s)

    algo_frame_s = tb.Frame(card_search)
    algo_frame_s.pack(fill="x", padx=5, pady=5)
    tb.Label(algo_frame_s, text="Algorithm:").pack(side="left", padx=(0,5))
    search_algos = ["Linear Search","Binary Search"]
    sel_search = tb.StringVar(value=search_algos[0])
    combo_search = tb.Combobox(algo_frame_s, values=search_algos, textvariable=sel_search, width=20, state="readonly")
    combo_search.pack(side="left", padx=(0,10))
    info_lbl_s = tb.Label(algo_frame_s, text="", font=("Inter",9), foreground="gray")
    info_lbl_s.pack(side="left", fill="x", expand=True)
    
    def update_info_s(e=None):
        info_lbl_s.config(text=ALGO_INFO.get(sel_search.get(),""))
    combo_search.bind("<<ComboboxSelected>>", update_info_s)
    update_info_s()

    btn_frame_s = tb.Frame(card_search)
    btn_frame_s.pack(pady=8, padx=5)
    run_btn_s = tb.Button(btn_frame_s, text="▶ Search & Visualize", bootstyle=SUCCESS, width=15)
    run_btn_s.pack(side="left", padx=5)
    clear_btn_s = tb.Button(btn_frame_s, text="🗑 Clear", bootstyle=DANGER, width=10)
    clear_btn_s.pack(side="left", padx=5)

    viz_frame_search = tb.Labelframe(tab_search, text="🎨 Visual Representation", padding=10, bootstyle="info")
    viz_frame_search.pack(fill="both", expand=True, padx=10, pady=5)
    
    canvas_search = tk.Canvas(viz_frame_search, bg="#2c3e50", height=150, highlightthickness=0)
    canvas_search.pack(fill="both", expand=True, padx=5, pady=5)
    search_viz = SearchVisualizer(canvas_search, width=1100, height=150)

    metrics_frame_s = tb.Labelframe(tab_search, text="Performance Metrics", padding=5, bootstyle="success")
    metrics_frame_s.pack(fill="x", padx=10, pady=5)
    met_display_s = tb.Frame(metrics_frame_s)
    met_display_s.pack(fill="x")
    metric_labels_s = {}
    for i, (key, lbl) in enumerate([("time","⏱ Time:"),("comp","🔄 Comparisons:"),("result","📍 Result:")]):
        tb.Label(met_display_s, text=lbl, font=("Inter",9,"bold")).grid(row=0, column=i*2, sticky="w", padx=(0,5))
        metric_labels_s[key] = tb.Label(met_display_s, text="—", font=("Inter",9), foreground="cyan")
        metric_labels_s[key].grid(row=0, column=i*2+1, sticky="w", padx=(0,15))

    tb.Label(tab_search, text="Output:", font=("Inter",10,"bold")).pack(anchor="w", padx=15, pady=(5,2))
    out_frame_s = tb.Frame(tab_search, relief="solid", borderwidth=1)
    out_frame_s.pack(fill="x", padx=10, pady=5)
    output_search = tb.Text(out_frame_s, wrap="word", height=3, font=("Consolas",10), bd=0)
    output_search.pack(side="left", fill="both", expand=True)
    scroll_search = tb.Scrollbar(out_frame_s, command=output_search.yview)
    output_search.configure(yscrollcommand=scroll_search.set)
    scroll_search.pack(side="right", fill="y")

    def run_search():
        output_search.delete("1.0","end")
        try:
            arr = [int(x.strip()) for x in entry_search.get().split(",") if x.strip()]
            target = int(entry_target.get().strip())
            if not arr: raise ValueError()
        except:
            Messagebox.show_error("Input Error", "Enter valid data.")
            return
        
        search_viz.draw_array(arr, target=target)
        app.update()
        time.sleep(0.3)
        
        tracker = AlgorithmTracker()
        algo = sel_search.get()
        
        start = time.perf_counter()
        if algo == "Linear Search":
            result = linear_search(arr, target, tracker)
        else:
            result = binary_search(arr, target, tracker)
        end = time.perf_counter()
        tracker.time_taken = (end-start)*1000
        
        if tracker.steps:
            for step_data in tracker.steps:
                if algo == "Linear Search":
                    checking = step_data.get('checking')
                    found = step_data.get('found', False)
                    
                    if found:
                        search_viz.draw_array(arr, target=target, found_index=checking)
                    else:
                        search_viz.draw_array(arr, target=target, checking_index=checking)
                else:
                    left = step_data.get('left')
                    right = step_data.get('right')
                    mid = step_data.get('mid')
                    found = step_data.get('found', False)
                    
                    if found:
                        search_viz.draw_array(arr, target=target, found_index=mid,
                                            binary_left=left, binary_right=right, binary_mid=mid)
                    else:
                        search_viz.draw_array(arr, target=target,
                                            binary_left=left, binary_right=right, binary_mid=mid)
                
                app.update()
                time.sleep(0.4)
        else:
            search_viz.draw_array(arr, target=target, found_index=result if result != -1 else None)
        
        metric_labels_s["time"].config(text=f"{tracker.time_taken:.3f} ms")
        metric_labels_s["comp"].config(text=str(tracker.comparisons))
        metric_labels_s["result"].config(text=f"Index {result}" if result != -1 else "Not Found")
        
        output_search.insert("end", f"Array: {arr} | Target: {target}\n", "bold")
        if result != -1:
            output_search.insert("end", f"✓ Found at index {result} | ", "success")
        else:
            output_search.insert("end", "✗ Not found | ", "error")
        output_search.insert("end", f"{sel_search.get()} | Comparisons: {tracker.comparisons} | Time: {tracker.time_taken:.3f}ms")
        output_search.tag_config("bold", font=("Consolas",10,"bold"))
        output_search.tag_config("success", foreground="lightgreen")
        output_search.tag_config("error", foreground="orange")
        
        last_results["search"] = f"{sel_search.get()}\nArray: {arr}\nTarget: {target}\nResult: {result}"

    def clear_search():
        entry_search.delete(0,'end')
        entry_target.delete(0,'end')
        output_search.delete("1.0","end")
        canvas_search.delete("all")
        for lbl in metric_labels_s.values(): lbl.config(text="—")

    run_btn_s.configure(command=run_search)
    clear_btn_s.configure(command=clear_search)

    # ============================================================
    # GRAPH TAB
    # ============================================================
    tab_graph = tb.Frame(nb)
    nb.add(tab_graph, text="🕸 Graph Traversal")
    
    top_frame_graph = tb.Frame(tab_graph)
    top_frame_graph.pack(fill="x", padx=10, pady=10)
    
    card_graph = tb.Labelframe(top_frame_graph, text="Graph Controls", padding=10, bootstyle="primary")
    card_graph.pack(fill="x")

    tb.Label(card_graph, text="Graph (format: A:B,C B:D,E):").pack(anchor="w", padx=5, pady=2)
    entry_graph = tb.Entry(card_graph, width=70, font=("Inter",10))
    entry_graph.pack(fill="x", padx=5, pady=3)
    tb.Label(card_graph, text="Start Node:").pack(anchor="w", padx=5, pady=2)
    entry_start = tb.Entry(card_graph, width=20, font=("Inter",10))
    entry_start.pack(anchor="w", padx=5, pady=3)

    ex_frame_g = tb.Frame(card_graph)
    ex_frame_g.pack(fill="x", padx=5, pady=3)
    tb.Label(ex_frame_g, text="Example:").pack(side="left", padx=(0,5))
    ex_var_g = tb.StringVar(value="Select...")
    ex_combo_g = tb.Combobox(ex_frame_g, textvariable=ex_var_g, values=list(EXAMPLES["graph"].keys()), width=18, state="readonly")
    ex_combo_g.pack(side="left")
    
    def load_ex_g(e=None):
        if ex_var_g.get() in EXAMPLES["graph"]:
            data, start = EXAMPLES["graph"][ex_var_g.get()]
            entry_graph.delete(0,'end')
            entry_graph.insert(0, data)
            entry_start.delete(0,'end')
            entry_start.insert(0, start)
            try:
                graph = parse_graph(data)
                graph_viz.calculate_positions(graph, start)
                graph_viz.draw_graph(graph, start)
            except:
                pass
    ex_combo_g.bind("<<ComboboxSelected>>", load_ex_g)

    algo_frame_g = tb.Frame(card_graph)
    algo_frame_g.pack(fill="x", padx=5, pady=5)
    tb.Label(algo_frame_g, text="Algorithm:").pack(side="left", padx=(0,5))
    graph_algos = ["BFS","DFS"]
    sel_graph = tb.StringVar(value=graph_algos[0])
    combo_graph = tb.Combobox(algo_frame_g, values=graph_algos, textvariable=sel_graph, width=20, state="readonly")
    combo_graph.pack(side="left", padx=(0,10))
    info_lbl_g = tb.Label(algo_frame_g, text="", font=("Inter",9), foreground="gray")
    info_lbl_g.pack(side="left", fill="x", expand=True)
    
    def update_info_g(e=None):
        info_lbl_g.config(text=ALGO_INFO.get(sel_graph.get(),""))
    combo_graph.bind("<<ComboboxSelected>>", update_info_g)
    update_info_g()

    btn_frame_g = tb.Frame(card_graph)
    btn_frame_g.pack(pady=8, padx=5)
    run_btn_g = tb.Button(btn_frame_g, text="▶ Traverse & Visualize", bootstyle=SUCCESS, width=15)
    run_btn_g.pack(side="left", padx=5)
    clear_btn_g = tb.Button(btn_frame_g, text="🗑 Clear", bootstyle=DANGER, width=10)
    clear_btn_g.pack(side="left", padx=5)

    viz_frame_graph = tb.Labelframe(tab_graph, text="🎨 Visual Representation", padding=10, bootstyle="info")
    viz_frame_graph.pack(fill="both", expand=True, padx=10, pady=5)
    
    canvas_graph = tk.Canvas(viz_frame_graph, bg="#2c3e50", height=400, highlightthickness=0)
    canvas_graph.pack(fill="both", expand=True, padx=5, pady=5)
    graph_viz = GraphVisualizer(canvas_graph, width=1100, height=400)

    tb.Label(tab_graph, text="Output:", font=("Inter",10,"bold")).pack(anchor="w", padx=15, pady=(5,2))
    out_frame_g = tb.Frame(tab_graph, relief="solid", borderwidth=1)
    out_frame_g.pack(fill="x", padx=10, pady=5)
    output_graph = tb.Text(out_frame_g, wrap="word", height=3, font=("Consolas",10), bd=0)
    output_graph.pack(side="left", fill="both", expand=True)
    scroll_graph = tb.Scrollbar(out_frame_g, command=output_graph.yview)
    output_graph.configure(yscrollcommand=scroll_graph.set)
    scroll_graph.pack(side="right", fill="y")

    def run_graph():
        output_graph.delete("1.0","end")
        text = entry_graph.get().strip()
        start = entry_start.get().strip()
        if not text or not start:
            Messagebox.show_error("Input Error", "Enter graph and start node.")
            return
        try:
            graph = parse_graph(text)
        except Exception as e:
            Messagebox.show_error("Parse Error", str(e))
            return
        if start not in graph:
            graph[start] = []
        
        graph_viz.calculate_positions(graph, start)
        graph_viz.draw_graph(graph, start)
        app.update()
        time.sleep(0.5)
        
        tracker = AlgorithmTracker()
        t1 = time.perf_counter()
        result = graph_bfs(graph, start, tracker) if sel_graph.get()=="BFS" else graph_dfs(graph, start, tracker)
        t2 = time.perf_counter()
        
        if tracker.steps:
            for step_data in tracker.steps:
                visited = step_data.get('visited', [])
                current = step_data.get('current')
                
                graph_viz.draw_graph(graph, start, visited_order=visited, current_node=current)
                app.update()
                time.sleep(0.5)
        else:
            graph_viz.draw_graph(graph, start, visited_order=result)
        
        output_graph.insert("end", f"Start: {start} | Algorithm: {sel_graph.get()}\n", "bold")
        output_graph.insert("end", f"Traversal Order: {' → '.join(result)}\n", "result")
        output_graph.insert("end", f"✓ Visited {len(result)} nodes | Time: {(t2-t1)*1000:.3f}ms", "success")
        output_graph.tag_config("bold", font=("Consolas",10,"bold"))
        output_graph.tag_config("result", foreground="lightgreen", font=("Consolas",10,"bold"))
        output_graph.tag_config("success", foreground="lightgreen")
        
        last_results["graph"] = f"{sel_graph.get()}\nGraph: {text}\nStart: {start}\nTraversal: {result}"

    def clear_graph():
        entry_graph.delete(0,'end')
        entry_start.delete(0,'end')
        output_graph.delete("1.0","end")
        canvas_graph.delete("all")

    run_btn_g.configure(command=run_graph)
    clear_btn_g.configure(command=clear_graph)

    return app


if __name__ == "__main__":
    app = create_app()
    app.mainloop()
