"""
Recon-X Module : Domain & DNS
WHOIS lookup, DNS resolution, SPF/DKIM/DMARC checks.
"""

import whois
import dns.resolver
from datetime import datetime

class DomainDNSModule:
    def __init__(self, target, output_dir):
        self.target = target
        self.output_dir = output_dir
        self.results = {
            "module": "domain_dns",
            "target": target,
            "timestamp": datetime.now().isoformat(),
            "data": {}
        }

    def run(self):
        print(f"\n[+] Running Domain & DNS module for {self.target}...")
        self._whois_lookup()
        self._dns_resolution()
        self._spf_check()
        self._dkim_check()
        self._dmarc_check()
        return self.results

    def _whois_lookup(self):
        print("[*] WHOIS lookup...")
        try:
            w = whois.whois(self.target)
            self.results["data"]["whois"] = {
                "registrar": w.registrar,
                "creation_date": str(w.creation_date),
                "expiration_date": str(w.expiration_date),
                "name_servers": w.name_servers
            }
            print(f"    Registrar: {w.registrar}")
        except Exception as e:
            self.results["data"]["whois"] = {"error": str(e)}
            print(f"    [!] WHOIS failed: {e}")

    def _dns_resolution(self):
        print("[*] DNS resolution...")
        records = {}
        for rtype in ["A", "AAAA", "MX", "NS", "TXT", "CNAME"]:
            try:
                answers = dns.resolver.resolve(self.target, rtype)
                records[rtype] = [str(a) for a in answers]
                print(f"    {rtype}: {len(records[rtype])} record(s)")
            except:
                records[rtype] = []
        self.results["data"]["dns"] = records

    def _spf_check(self):
        print("[*] SPF check...")
        try:
            for r in dns.resolver.resolve(self.target, "TXT"):
                if "v=spf1" in str(r):
                    self.results["data"]["spf"] = {"record": str(r), "present": True}
                    print("    SPF found")
                    return
            self.results["data"]["spf"] = {"present": False}
        except:
            self.results["data"]["spf"] = {"present": False}

    def _dkim_check(self):
        print("[*] DKIM check...")
        selectors = ["default", "google", "selector1", "selector2"]
        found = []
        for s in selectors:
            try:
                answers = dns.resolver.resolve(f"{s}._domainkey.{self.target}", "TXT")
                found.append({"selector": s, "record": str(answers[0])})
            except:
                pass
        self.results["data"]["dkim"] = {"present": len(found) > 0, "selectors": found}
        print(f"    DKIM: {len(found)} selector(s)")

    def _dmarc_check(self):
        print("[*] DMARC check...")
        try:
            for r in dns.resolver.resolve(f"_dmarc.{self.target}", "TXT"):
                if "v=DMARC1" in str(r):
                    self.results["data"]["dmarc"] = {"record": str(r), "present": True}
                    print("    DMARC found")
                    return
            self.results["data"]["dmarc"] = {"present": False}
        except:
            self.results["data"]["dmarc"] = {"present": False}
