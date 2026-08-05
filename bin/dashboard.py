#!/usr/bin/env python3
import subprocess, sys, os
ws = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.exit(subprocess.call([sys.executable, os.path.join(ws, ".agents", "skills", "generate-dashboard", "scripts", "build_dashboard.py")]))
