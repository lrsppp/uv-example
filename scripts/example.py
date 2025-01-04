# touch example.py && uv add --script example.py 'numpy'
# run via: uv run example.py
# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "numpy",
# ]
# ///
import numpy as np  # will not be installed into venv when using uv run example.py

print(np.add(5, [4, 3]))
