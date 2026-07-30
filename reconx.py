#!/usr/bin/env python3
"""
🔍 Recon-X — Automated OSINT Toolkit
Usage: python reconx.py --target example.com
"""

import click
import json
import os
import sys
from datetime import datetime
from pathlib import Path

try:
    from rich.console import Console
    from rich.table import Table
    from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
    from rich.panel import Panel
    from rich import print as rprint
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False
    print("[!] Install 'rich' for better UI: pip install rich")

from modules.domain_dns import DomainDNSModule
from modules.subdomain_discovery import SubdomainDiscoveryModule
from modules.port_scanning import PortScanningModule
from modules.email_accounts import EmailAccountsModule
from modules.web_surface import WebSurfaceModule
from modules.social_media import SocialMediaModule
from modules.report import ReportModule

VERSION = "1.0.0"
CONFIG_FILE = "config.json"
TOKEN_FILE = "reconx.token"
BANNER = """
╔══════════════════════════════════════════════╗
║                                              ║
║   ██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗
║   ██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║
║   ██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║
║   ██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║
║   ██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║
║   ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝
║                                              ║
║        Automated OSINT Toolkit v1.0          ║
║                                              ║
╚══════════════════════════════════════════════╝
"""

def load_config():
    if not os.path.exists(CONFIG_FILE):
        rprint("[red][!][/red] Config file not found.")
        sys.exit(1)
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)

def check_token():
    config = load_config()
    if not config.get("token_required", True):
        return True
    if not os.path.exists(TOKEN_FILE):
        rprint("[red][!][/red] Authorization token required.")
        return False
    with open(TOKEN_FILE, "r") as f:
        token = f.read().strip()
    if token != "RECON_X_AUTHORIZED":
        rprint("[red][!][/red] Invalid token.")
        return False
    return True

@click.command()
@click.option("--target", "-t", required=True, help="Target domain (e.g., example.com)")
@click.option("--output", "-o", default="./output", help="Output directory")
@click.option("--module", "-m", multiple=True, help="Specific module to run")
@click.version_option(version=VERSION, prog_name="Recon-X")
def main(target, output, module):
    """🔍 Recon-X — Automated OSINT Toolkit for Attack Surface Analysis"""
    
    console = Console() if RICH_AVAILABLE else None
    
    if not check_token():
        sys.exit(1)
    
    config = load_config()
    output_dir = output or config.get("output_dir", "./output")
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    if RICH_AVAILABLE:
        console.print(BANNER, style="bold magenta")
        console.print(f"[cyan][*][/cyan] Target : [bold]{target}[/bold]")
        console.print(f"[cyan][*][/cyan] Output : [bold]{output_dir}[/bold]")
        console.print(f"[cyan][*][/cyan] Time   : [bold]{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}[/bold]")
        console.print("─" * 50, style="dim")
    else:
        print(BANNER)
        print(f"[*] Target : {target}")
        print(f"[*] Output : {output_dir}")
        print(f"[*] Time   : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("-" * 50)
    
    # Initialiser les modules
    all_modules = {
        "domain_dns": DomainDNSModule(target, output_dir),
        "subdomain_discovery": SubdomainDiscoveryModule(target, output_dir),
        "port_scanning": PortScanningModule(target, output_dir),
        "email_accounts": EmailAccountsModule(target, output_dir),
        "web_surface": WebSurfaceModule(target, output_dir),
        "social_media": SocialMediaModule(target, output_dir),
    }
    
    # Filtrer si des modules spécifiques sont demandés
    if module:
        modules_to_run = {k: v for k, v in all_modules.items() if k in module}
    else:
        modules_to_run = all_modules
    
    # Exécuter les modules
    all_results = []
    
    if RICH_AVAILABLE:
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            console=console
        ) as progress:
            task = progress.add_task("[cyan]Running modules...", total=len(modules_to_run))
            
            for name, mod in modules_to_run.items():
                progress.update(task, description=f"[cyan]Running {name}...")
                results = mod.run()
                all_results.append(results)
                progress.advance(task)
    else:
        for name, mod in modules_to_run.items():
            results = mod.run()
            all_results.append(results)
    
    # Générer les rapports
    report = ReportModule(target, output_dir, all_results)
    report.run()
    
    # Résumé final
    if RICH_AVAILABLE:
        console.print("─" * 50, style="dim")
        console.print("[bold green][✓][/bold green] Recon-X completed successfully!")
        console.print(f"[cyan][i][/cyan] Reports saved in [bold]{output_dir}[/bold]")
    else:
        print("-" * 50)
        print(f"[✓] Recon-X completed!")
        print(f"[i] Reports saved in {output_dir}")

if __name__ == "__main__":
    main()
