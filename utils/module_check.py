# module_check.py
import sys, os

def ensure_package_context(relative_path=".."):
    """
    Ensure the script can run even if not executed with `-m`.
    Adds project root to sys.path and prints a warning if needed.
    """
    if __package__ is None or __spec__ is None:
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), relative_path))
        sys.path.append(project_root)
        print("[Warning] Running outside of package context. sys.path fix applied.")
