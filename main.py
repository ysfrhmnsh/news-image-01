"""Copy the news image to the output directory.

The entry is the image entry.png in this repository; the program writes
exactly those bytes to /output/entry.png (or $MAKEFUN_OUTPUT_DIR/entry.png).
A plain copy is deterministic: both runs write identical bytes.
"""
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
OUT = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.png")

os.makedirs(os.path.dirname(OUT), exist_ok=True)
shutil.copyfile(SRC, OUT)
