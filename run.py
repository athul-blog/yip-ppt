import subprocess
import os

# --------- Step 1: Open the PPTX file ---------
pptx_path = "example.pptx"  # Replace with your PPTX file path

try:
    # Opens the PPTX with the default app (LibreOffice, PowerPoint via Wine, etc.)
    subprocess.run(["xdg-open", pptx_path], check=True)
    print(f"Opened presentation: {pptx_path}")
except Exception as e:
    print(f"Error opening presentation: {e}")  # Fixed syntax
