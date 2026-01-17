import os
import sys

# Mimic the notebook's behavior
os.chdir("../")
print(f"Current working directory: {os.getcwd()}")
print(f"Python executable: {sys.executable}")

try:
    from textSummarizer.utils.common import read_yaml
    print("SUCCESS: read_yaml imported successfully")
except ImportError as e:
    print(f"FAILURE: {e}")
except Exception as e:
    print(f"FAILURE: {e}")
