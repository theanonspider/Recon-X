"""
Recon-X Module : Scan de ports
Scan des ports courants et détection de services.
"""

import socket
from datetime import datetime

class ModuleScanPorts:
    def __init__(self, cible, dossier_sortie):
        self.cible = cible
        self.dossier_sortie = dossier_sortie
        self.resultats = {
            "module": "scan_ports",
            "cible": cible,
            "horodatage": datetime.now().isoformat(),
            "donnees": {"ports_ouverts": []}
        }
        
        self.ports_communs = {
            21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP",
            53: "DNS", 80: "HTTP", 110: "POP3", 143: "IMAP",
            443: "HTTPS", 445: "SMB", 993: "IMAPS", 995: "POP3S",
            3306: "MySQL", 3389: "RDP", 5432: "PostgreSQL",
            6379: "Redis", 8080: "HTTP-Alt", 8443: "HTTPS-Alt",
            27017: "MongoDB"
        }

    def executer(self):
        print(f"\n[+] Module Scan de ports pour {self.cible}...")
        
        # Résoudre le domaine en IP
        try:
            ip = socket.gethostbyname(self.cible)
            print(f"[*] IP résolue : {ip}")
        except:
            print(f"[!] Impossible de résoudre {self.cible}")
            return self.resultats
        
        for port, service in self.ports_communs.items():
            self._tester_port(ip, port, service)
        
        return self.resultats

    def _tester_port(self, ip, port, service):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            resultat = sock.connect_ex((ip, port))
            if resultat == 0:
                banniere = self._recuperer_banniere(sock)
                self.resultats["donnees"]["ports_ouverts"].append({
                    "port": port,
                    "service": service,
                    "banniere": banniere
                })
                print(f"    [+] {port}/tcp - {service} {banniere if banniere else ''}")
            sock.close()
        except:
            pass

    def _recuperer_banniere(self, sock):
        try:
            sock.settimeout(1)
            sock.send(b"HEAD / HTTP/1.0\r\n\r\n")
            banniere = sock.recv(1024).decode("utf-8", errors="ignore").strip()
            return banniere[:100] if banniere else ""
        except:
            return ""
