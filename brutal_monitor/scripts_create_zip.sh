#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
python3 - <<'PY'
import os, zipfile
root='brutal_monitor'
out='brutal_monitor.zip'
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as z:
    for base, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in {'__pycache__', '.git'}]
        for f in files:
            if f.endswith(('.pyc', '.pyo')):
                continue
            p=os.path.join(base,f)
            z.write(p,p)
print('Generado', out)
PY
