"""
Recon-X Module : Port Scanning
Common port scanning and service banner grabbing.
"""

import socket
from datetime import datetime

class PortScanningModule:
    def __init__(self, target, output_dir):
        self.target = target
        self.output_dir = output_dir
        self.results = {
            "module": "port_scanning",
            "target": target,
            "timestamp": datetime.now().isoformat(),
            "data": {"open_ports": []}
        }
        self.common_ports = {
            21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP",
            53: "DNS", 80: "HTTP", 110: "POP3", 143: "IMAP",
            443: "HTTPS", 445: "SMB", 993: "IMAPS", 995: "POP3S",
            3306: "MySQL", 3389: "RDP", 5432: "PostgreSQL",
            6379: "Redis", 8080: "HTTP-Alt", 8443: "HTTPS-Alt",
            27017: "MongoDB"
        }

    def run(self):
        print(f"\n[+] Running Port Scanning for {self.target}...")
        try:
            ip = socket.gethostbyname(self.target)
            print(f"[*] Resolved IP: {ip}")
        except:
            print(f"[!] Could not resolve {self.target}")
            return self.results
        for port, service in self.common_ports.items():
            self._test_port(ip, port, service)
        return self.results

    def _test_port(self, ip, port, service):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            result = sock.connect_ex((ip, port))
            if result == 0:
                banner = self._grab_banner(sock)
                self.results["data"]["open_ports"].append({
                    "port": port, "service": service, "banner": banner
                })
                print(f"    [+] {port}/tcp - {service} {banner if banner else ''}")
            sock.close()
        except:
            pass

    def _grab_banner(self, sock):
        try:
            sock.settimeout(1)
            sock.send(b"HEAD / HTTP/1.0\r\n\r\n")
            banner = sock.recv(1024).decode("utf-8", errors="ignore").strip()
            return banner[:100] if banner else ""
        except:
            return ""
