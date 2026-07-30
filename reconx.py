#!/usr/bin/env python3
"""
Recon-X : Automated OSINT Toolkit
Usage: python reconx.py --target example.com
"""

import click
import json
import os
import sys
from datetime import datetime
from pathlib import Path

VERSION = "1.0.0"
CONFIG_FILE = "config.json"
TOKEN_FILE = "reconx.token"

def load_config():
    if not os.path.exists(CONFIG_FILE):
        print(f"[!] Config file {CONFIG_FILE} not found.")
        sys.exit(1)
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)

def check_token():
    config = load_config()
    if not config.get("token_required", True):
        return True
    if not os.path.exists(TOKEN_FILE):
        print(f"[!] Authorization token required. Create {TOKEN_FILE}")
        return False
    with open(TOKEN_FILE, "r") as f:
        token = f.read().strip()
    if token != "RECON_X_AUTHORIZED":
        print("[!] Invalid token.")
        return False
    return True

@click.command()
@click.option("--target", "-t", required=True, help="Target domain (e.g., example.com)")
@click.option("--output", "-o", default="./output", help="Output directory")
@click.option("--module", "-m", multiple=True, help="Specific module to run")
@click.version_option(version=VERSION, prog_name="Recon-X")
def main(target, output, module):
    """Recon-X — Automated OSINT Toolkit for Attack Surface Analysis"""
    
    if not check_token():
        sys.exit(1)
    
    config = load_config()
    output_dir = output or config.get("output_dir", "./output")
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    print(f"""
╔══════════════════════════════════════════╗
║        🔍 Recon-X v{VERSION}                  ║
║   Automated OSINT Toolkit               ║
╚══════════════════════════════════════════╝
    """)
    print(f"[*] Target : {target}")
    print(f"[*] Output : {output_dir}")
    print(f"[*] Time   : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)
    
    # Ici viendront les modules
    print("[✓] Recon-X initialized successfully.")
    print("[i] Modules will be added in next updates.")

if __name__ == "__main__":
    main()
