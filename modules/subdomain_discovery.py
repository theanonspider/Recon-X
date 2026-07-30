"""
Recon-X Module : Subdomain Discovery
Bruteforce and Certificate Transparency scraping.
"""

import requests
import dns.resolver
from datetime import datetime

class SubdomainDiscoveryModule:
    def __init__(self, target, output_dir):
        self.target = target
        self.output_dir = output_dir
        self.results = {
            "module": "subdomain_discovery",
            "target": target,
            "timestamp": datetime.now().isoformat(),
            "data": {"subdomains": []}
        }

    def run(self):
        print(f"\n[+] Running Subdomain Discovery for {self.target}...")
        self._certificate_transparency()
        self._bruteforce()
        return self.results

    def _certificate_transparency(self):
        print("[*] Querying crt.sh...")
        try:
            url = f"https://crt.sh/?q=%25.{self.target}&output=json"
            response = requests.get(url, timeout=30)
            if response.status_code == 200:
                data = response.json()
                subdomains = set()
                for entry in data:
                    name = entry.get("name_value", "")
                    for sub in name.split("\n"):
                        if self.target in sub:
                            subdomains.add(sub.strip().lower())
                self.results["data"]["certificate_transparency"] = list(subdomains)
                print(f"    crt.sh: {len(subdomains)} subdomain(s)")
        except Exception as e:
            print(f"    [!] crt.sh failed: {e}")

    def _bruteforce(self):
        print("[*] Bruteforcing subdomains...")
        wordlist = [
            "www", "mail", "ftp", "admin", "api", "dev", "staging",
            "blog", "shop", "cdn", "remote", "vpn", "portal", "webmail",
            "secure", "test", "app", "mobile", "m", "docs", "support"
        ]
        found = []
        for prefix in wordlist:
            sub = f"{prefix}.{self.target}"
            try:
                dns.resolver.resolve(sub, "A")
                found.append(sub)
                print(f"    [+] {sub}")
            except:
                pass
        self.results["data"]["bruteforce"] = found
        print(f"    Bruteforce: {len(found)} found")
