# -*- coding: utf-8 -*-
"""
Main entry point for Aviation Exam Platform Dataset Generator.
Invokes the complete suite aligning 1:1 with official military bold face PDFs.
"""
import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCRIPTS_DIR = os.path.join(BASE_DIR, "scripts")
if SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, SCRIPTS_DIR)

# Ensure execution runs from repository root
os.chdir(BASE_DIR)

try:
    from scripts.build_all_data_perfect import main as build_master
except ImportError:
    from build_all_data_perfect import main as build_master

if __name__ == "__main__":
    print("Executing Aviation Exam Platform Master Data Generator...")
    build_master()
    print("Master dataset generation complete!")
