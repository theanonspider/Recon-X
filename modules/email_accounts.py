"""
Recon-X Module : Email & Accounts
Public email search and Have I Been Pwned verification.
"""

import requests
from datetime import datetime

class EmailAccountsModule:
    def __init__(self, target, output_dir):
        self.target = target
        self.output_dir = output_dir
        self.results = {
            "module": "email_accounts",
            "target": target,
            "timestamp": datetime.now().isoformat(),
            "data": {"emails_found": [], "breaches": []}
        }
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": "Recon-X/1.0 (Educational OSINT)"})

    def run(self):
        print(f"\n[+] Running Email & Accounts for {self.target}...")
        self._search_emails()
        self._check_breaches()
        return self.results

    def _search_emails(self):
        print("[*] Generating email patterns...")
        patterns = [
            f"contact@{self.target}", f"info@{self.target}",
            f"admin@{self.target}", f"support@{self.target}",
            f"security@{self.target}", f"abuse@{self.target}",
            f"webmaster@{self.target}", f"postmaster@{self.target}"
        ]
        self.results["data"]["emails_found"] = patterns
        print(f"    {len(patterns)} email patterns generated")

    def _check_breaches(self):
        print("[*] Checking Have I Been Pwned...")
        for email in self.results["data"]["emails_found"][:3]:
            try:
                url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
                response = self.session.get(url, timeout=10)
                if response.status_code == 200:
                    breaches = response.json()
                    self.results["data"]["breaches"].append({
                        "email": email,
                        "breaches": [b["Name"] for b in breaches]
                    })
                    print(f"    [!] {email}: {len(breaches)} breach(es)")
                elif response.status_code == 404:
                    print(f"    [✓] {email}: No breaches")
            except:
                pass
