"""
Recon-X Module : Report Generation
Generates HTML and JSON reports from collected data.
"""

import json
import os
from datetime import datetime

class ReportModule:
    def __init__(self, target, output_dir, results):
        self.target = target
        self.output_dir = output_dir
        self.results = results

    def run(self):
        print(f"\n[+] Generating reports...")
        self._save_json()
        self._save_html()
        print(f"[✓] Reports saved in {self.output_dir}")

    def _save_json(self):
        filepath = os.path.join(self.output_dir, f"recon_{self.target}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
        with open(filepath, "w") as f:
            json.dump(self.results, f, indent=2)
        print(f"    JSON: {filepath}")

    def _save_html(self):
        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Recon-X Report - {self.target}</title>
    <style>
        body {{ background:#0a0a0f; color:#ccc; font-family:monospace; max-width:800px; margin:40px auto; padding:20px; }}
        h1 {{ color:#9b59b6; }} h2 {{ color:#7d3c98; border-bottom:1px solid #2a1a3e; padding-bottom:5px; }}
        pre {{ background:#0f0f1a; padding:15px; border-left:3px solid #6c3483; overflow-x:auto; }}
        .footer {{ margin-top:40px; color:#444; text-align:center; font-size:0.8em; }}
    </style>
</head>
<body>
    <h1>🔍 Recon-X Report</h1>
    <p>Target: {self.target}</p>
    <p>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
    <h2>Raw Data</h2>
    <pre>{json.dumps(self.results, indent=2)}</pre>
    <div class="footer">Recon-X | Educational OSINT Tool</div>
</body>
</html>"""
        filepath = os.path.join(self.output_dir, f"recon_{self.target}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html")
        with open(filepath, "w") as f:
            f.write(html)
        print(f"    HTML: {filepath}")
