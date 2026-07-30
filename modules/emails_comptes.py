"""
Recon-X Module : Emails & Comptes
Recherche d'emails publics, vérification Have I Been Pwned, patterns d'emails.
"""

import requests
from datetime import datetime

class ModuleEmailsComptes:
    def __init__(self, cible, dossier_sortie):
        self.cible = cible
        self.dossier_sortie = dossier_sortie
        self.resultats = {
            "module": "emails_comptes",
            "cible": cible,
            "horodatage": datetime.now().isoformat(),
            "donnees": {
                "emails_trouves": [],
                "fuites": []
            }
        }
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Recon-X/1.0 (OSINT éducatif)"
        })

    def executer(self):
        print(f"\n[+] Module Emails & Comptes pour {self.cible}...")
        self._recherche_emails()
        self._verification_fuites()
        return self.resultats

    def _recherche_emails(self):
        print("[*] Recherche d'emails publics...")
        patterns = [
            f"contact@{self.cible}",
            f"info@{self.cible}",
            f"admin@{self.cible}",
            f"support@{self.cible}",
            f"security@{self.cible}",
            f"abuse@{self.cible}",
            f"webmaster@{self.cible}",
            f"postmaster@{self.cible}",
        ]
        self.resultats["donnees"]["emails_trouves"] = patterns
        print(f"    {len(patterns)} patterns d'emails générés")

    def _verification_fuites(self):
        print("[*] Vérification Have I Been Pwned...")
        emails_a_tester = self.resultats["donnees"]["emails_trouves"]
        for email in emails_a_tester[:3]:  # Limiter pour l'API
            try:
                url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
                reponse = self.session.get(url, timeout=10)
                if reponse.status_code == 200:
                    breaches = reponse.json()
                    self.resultats["donnees"]["fuites"].append({
                        "email": email,
                        "breaches": [b["Name"] for b in breaches]
                    })
                    print(f"    [!] {email} : {len(breaches)} fuite(s)")
                elif reponse.status_code == 404:
                    print(f"    [✓] {email} : Aucune fuite")
            except:
                pass
