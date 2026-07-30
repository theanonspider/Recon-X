"""
Recon-X Module : Domaine & DNS
Recherche WHOIS, résolution DNS, vérification SPF/DKIM/DMARC.
"""

import whois
import dns.resolver
from datetime import datetime

class ModuleDomaineDNS:
    def __init__(self, cible, dossier_sortie):
        self.cible = cible
        self.dossier_sortie = dossier_sortie
        self.resultats = {
            "module": "domaine_dns",
            "cible": cible,
            "horodatage": datetime.now().isoformat(),
            "donnees": {}
        }

    def executer(self):
        print(f"\n[+] Module Domaine & DNS pour {self.cible}...")
        self._whois()
        self._resolution_dns()
        self._verification_spf()
        self._verification_dkim()
        self._verification_dmarc()
        return self.resultats

    def _whois(self):
        print("[*] Recherche WHOIS...")
        try:
            w = whois.whois(self.cible)
            self.resultats["donnees"]["whois"] = {
                "registrar": w.registrar,
                "date_creation": str(w.creation_date),
                "date_expiration": str(w.expiration_date),
                "serveurs_noms": w.name_servers
            }
            print(f"    Registrar : {w.registrar}")
        except Exception as e:
            self.resultats["donnees"]["whois"] = {"erreur": str(e)}
            print(f"    [!] Échec WHOIS : {e}")

    def _resolution_dns(self):
        print("[*] Résolution DNS...")
        enregistrements = {}
        types_enr = ["A", "AAAA", "MX", "NS", "TXT", "CNAME"]
        for t in types_enr:
            try:
                reponses = dns.resolver.resolve(self.cible, t)
                enregistrements[t] = [str(r) for r in reponses]
                print(f"    {t} : {len(enregistrements[t])} enr.")
            except:
                enregistrements[t] = []
        self.resultats["donnees"]["dns"] = enregistrements

    def _verification_spf(self):
        print("[*] Vérification SPF...")
        try:
            for r in dns.resolver.resolve(self.cible, "TXT"):
                if "v=spf1" in str(r):
                    self.resultats["donnees"]["spf"] = {"enregistrement": str(r), "present": True}
                    print(f"    SPF trouvé")
                    return
            self.resultats["donnees"]["spf"] = {"present": False}
        except:
            self.resultats["donnees"]["spf"] = {"present": False}

    def _verification_dkim(self):
        print("[*] Vérification DKIM...")
        selecteurs = ["default", "google", "selector1", "selector2"]
        trouves = []
        for s in selecteurs:
            try:
                domaine = f"{s}._domainkey.{self.cible}"
                reponses = dns.resolver.resolve(domaine, "TXT")
                trouves.append({"selecteur": s, "enregistrement": str(reponses[0])})
            except:
                pass
        self.resultats["donnees"]["dkim"] = {"present": len(trouves) > 0, "selecteurs": trouves}
        print(f"    DKIM : {len(trouves)} sélecteur(s)")

    def _verification_dmarc(self):
        print("[*] Vérification DMARC...")
        try:
            for r in dns.resolver.resolve(f"_dmarc.{self.cible}", "TXT"):
                if "v=DMARC1" in str(r):
                    self.resultats["donnees"]["dmarc"] = {"enregistrement": str(r), "present": True}
                    print(f"    DMARC trouvé")
                    return
            self.resultats["donnees"]["dmarc"] = {"present": False}
        except:
            self.resultats["donnees"]["dmarc"] = {"present": False}
