"""
Recon-X Module : Web Surface
Light crawling, admin panel detection, technology fingerprinting.
"""

import requests
from datetime import datetime

class WebSurfaceModule:
    def __init__(self, target, output_dir):
        self.target = target
        self.output_dir = output_dir
        self.results = {
            "module": "web_surface",
            "target": target,
            "timestamp": datetime.now().isoformat(),
            "data": {
                "pages_found": [],
                "admin_panels": [],
                "technologies": []
            }
        }
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": "Recon-X/1.0 (Educational OSINT)"})

    def run(self):
        print(f"\n[+] Running Web Surface for {self.target}...")
        self._crawl()
        self._detect_admin()
        self._detect_technologies()
        return self.results

    def _crawl(self):
        print("[*] Light crawling...")
        paths = ["/", "/robots.txt", "/sitemap.xml", "/.well-known/", "/login", "/admin"]
        for path in paths:
            try:
                url = f"https://{self.target}{path}"
                resp = self.session.get(url, timeout=10, allow_redirects=True)
                self.results["data"]["pages_found"].append({
                    "url": url, "code": resp.status_code, "size": len(resp.content)
                })
                if resp.status_code == 200:
                    print(f"    [+] {url} (200, {len(resp.content)} bytes)")
                else:
                    print(f"    [-] {url} ({resp.status_code})")
            except Exception as e:
                print(f"    [!] {path}: {e}")

    def _detect_admin(self):
        print("[*] Admin panel detection...")
        admin_paths = [
            "/admin", "/wp-admin", "/administrator", "/login",
            "/panel", "/dashboard", "/manage", "/backend"
        ]
        for path in admin_paths:
            try:
                url = f"https://{self.target}{path}"
                resp = self.session.get(url, timeout=10, allow_redirects=True)
                if resp.status_code in [200, 301, 302, 403]:
                    self.results["data"]["admin_panels"].append({
                        "url": url, "code": resp.status_code
                    })
                    print(f"    [!] Potential admin panel: {url} ({resp.status_code})")
            except:
                pass

    def _detect_technologies(self):
        print("[*] Technology detection...")
        try:
            resp = self.session.get(f"https://{self.target}/", timeout=10)
            headers = resp.headers
            if "X-Powered-By" in headers:
                self.results["data"]["technologies"].append(headers["X-Powered-By"])
            if "Server" in headers:
                self.results["data"]["technologies"].append(headers["Server"])
            content = resp.text.lower()
            if "wp-content" in content:
                self.results["data"]["technologies"].append("WordPress")
            if "joomla" in content:
                self.results["data"]["technologies"].append("Joomla")
            if "drupal" in content:
                self.results["data"]["technologies"].append("Drupal")
            print(f"    Technologies: {self.results['data']['technologies']}")
        except:
            pass
