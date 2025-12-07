"""
Example Data for Testing Algorithms
"""

EXAMPLES = {
    "sort": {
        "Random Small": "64, 34, 25, 12, 22, 11, 90",
        "Random Medium": "45, 23, 78, 12, 90, 34, 67, 89, 15, 56",
        "Nearly Sorted": "10, 20, 15, 30, 25, 40, 35, 50",
        "Reverse Order": "100, 90, 80, 70, 60, 50, 40, 30",
        "All Same": "5, 5, 5, 5, 5, 5, 5",
        "Large Dataset": "100, 45, 23, 67, 12, 89, 34, 56, 78, 90, 11, 55, 44, 33, 22, 99, 88, 77, 66, 15",
    },
    "search": {
        "Simple List": ("10, 20, 30, 40, 50, 60, 70, 80", "50"),
        "Large List": ("5, 15, 25, 35, 45, 55, 65, 75, 85, 95", "65"),
        "Not Found": ("10, 20, 30, 40, 50", "99"),
        "First Element": ("1, 5, 9, 13, 17, 21", "1"),
        "Last Element": ("2, 4, 6, 8, 10, 12, 14, 16", "16"),
    },
    "graph": {
        "Simple Tree": ("A:B,C B:D,E C:F,G", "A"),
        "Connected Graph": ("A:B,C B:D C:D,E D:E,F", "A"),
        "Complex Graph": ("A:B,C,D B:E,F C:G D:H E:I F:J G:K H:L", "A"),
        "Cyclic Graph": ("A:B,C B:D C:D D:A", "A"),
        "Disconnected": ("A:B B:C D:E E:F", "A"),
    }
}