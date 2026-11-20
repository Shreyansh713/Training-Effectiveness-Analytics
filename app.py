"""
D26: Training Effectiveness Data Analysis
Main Application Entry Point (Root Wrapper)
Executes dashboard/app.py seamlessly.
"""

import os
import sys

# Ensure dashboard directory is in path
dashboard_path = os.path.join(os.path.dirname(__file__), "dashboard")
if dashboard_path not in sys.path:
    sys.path.insert(0, dashboard_path)

# Execute the dashboard app
with open(os.path.join(dashboard_path, "app.py"), "r", encoding="utf-8") as f:
    code = compile(f.read(), os.path.join(dashboard_path, "app.py"), 'exec')
    exec(code)
