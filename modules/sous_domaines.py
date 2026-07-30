"""
Recon-X Module : Découverte de sous-domaines
Bruteforce intelligent, scraping Certificate Transparency, résolution DNS.
"""

import requests
import dns.resolver
from datetime import datetime

class ModuleSousDomaines:
    def __init__(self, cible, dossier_sortie):
        self.cible = cible
        self.dossier_sortie = dossier_sortie
        self.resultats = {
            "module": "sous_domaines",
            "cible": cible,
            "horodatage": datetime.now().isoformat(),
            "donnees": {"sous_domaines": []}
        }

    def executer(self):
        print(f"\n[+] Module Sous-domaines pour {self.cible}...")
        self._certificate_transparency()
        self._bruteforce()
        return self.resultats

    def _certificate_transparency(self):
        print("[*] Recherche Certificate Transparency (crt.sh)...")
        try:
            url = f"https://crt.sh/?q=%25.{self.cible}&output=json"
            reponse = requests.get(url, timeout=30)
            if reponse.status_code == 200:
                donnees = reponse.json()
                sous_domaines = set()
                for entree in donnees:
                    nom = entree.get("name_value", "")
                    for sous_dom in nom.split("\n"):
                        if self.cible in sous_dom:
                            sous_domaines.add(sous_dom.strip().lower())
                self.resultats["donnees"]["certificate_transparency"] = list(sous_domaines)
                print(f"    crt.sh : {len(sous_domaines)} sous-domaine(s)")
        except Exception as e:
            print(f"    [!] crt.sh échec : {e}")

    def _bruteforce(self):
        print("[*] Bruteforce sous-domaines...")
        wordlist = [
            "www", "mail", "ftp", "admin", "api", "dev", "staging",
            "blog", "shop", "cdn", "remote", "vpn", "portal", "webmail",
            "secure", "test", "app", "mobile", "m", "docs", "support"
        ]
        trouves = []
        for prefixe in wordlist:
            sous_dom = f"{prefixe}.{self.cible}"
            try:
                dns.resolver.resolve(sous_dom, "A")
                trouves.append(sous_dom)
                print(f"    [+] {sous_dom}")
            except:
                pass
        self.resultats["donnees"]["bruteforce"] = trouves
        print(f"    Bruteforce : {len(trouves)} trouvé(s)")
