import subprocess
import os
import sys

base = r"C:\Users\bruno\projects\from-dsi-to-pqc"
os.chdir(base)

def run(cmd):
    print(f"Running: {' '.join(cmd)}")
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding='latin1')
    return res.returncode, res.stdout

# 1. pdflatex pass 1
code, out = run(["pdflatex", "-interaction=nonstopmode", "book.tex"])
if code != 0:
    print("pdflatex pass 1 output tail:")
    print("\n".join(out.splitlines()[-25:]))
else:
    print("pdflatex pass 1 OK")

# 2. bibtex
code_b, out_b = run(["bibtex", "book"])
print("bibtex output tail:")
print("\n".join(out_b.splitlines()[-15:]))

# 3. pdflatex pass 2
code, out = run(["pdflatex", "-interaction=nonstopmode", "book.tex"])
print("pdflatex pass 2 OK" if code == 0 else "pdflatex pass 2 warning")

# 4. pdflatex pass 3
code, out = run(["pdflatex", "-interaction=nonstopmode", "book.tex"])
print("pdflatex pass 3 OK" if code == 0 else "pdflatex pass 3 error")

pdf_path = os.path.join(base, "book.pdf")
if os.path.exists(pdf_path):
    size = os.path.getsize(pdf_path)
    print(f"\nSUCCESS: Generated {pdf_path} ({size:,} bytes)")
else:
    print(f"\nFAILED: {pdf_path} not found")
    sys.exit(1)

