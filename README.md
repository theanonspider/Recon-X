
---

## 3️⃣ RECON-X V1 (7 modules)

```markdown
# 🔍 Recon-X — OSINT Tool

> ⚠️ **AVERTISSEMENT** — Usage exclusivement éducatif et défensif.  
> Toute utilisation non autorisée est **ILLÉGALE** et engage votre responsabilité.

---

## 📖 Pourquoi Recon-X ?

**Recon-X** est un outil OSINT modulaire pour la reconnaissance.  
Il collecte des informations publiques sur des cibles : domaines, sous‑domaines, emails, technologies, etc.

Parfait pour les **pentests**, la **veille concurrentielle** ou les **investigations**.

---

## 🧩 Modules (7)

| Module | Fonction |
|--------|----------|
| `domain_dns` | WHOIS, DNS, SPF/DKIM/DMARC |
| `subdomain` | Découverte de sous‑domaines (bruteforce, crt.sh) |
| `port_scan` | Scan de ports |
| `emails` | Recherche d’emails publics |
| `web_surface` | Crawling, panneaux admin, technologies |
| `report` | Rapports HTML/JSON |

---

## 🔐 Sécurité

```bash
echo "RECONX_AUTHORIZED" > reconx.token

⚙️ Installation
bash

git clone https://github.com/theanonspider/Recon-X.git
cd Recon-X
pip install -r requirements.txt
echo "RECONX_AUTHORIZED" > reconx.token

🚀 Exemples d’utilisation
bash

# 1. WHOIS + DNS
python reconx.py domain-dns -t example.com

# 2. Découverte de sous‑domaines
python reconx.py subdomain -t example.com

# 3. Scan de ports
python reconx.py port-scan -t example.com -p 1-1000

# 4. Recherche d’emails
python reconx.py emails -t example.com

# 5. Rapport complet
python reconx.py report -o ./reports -f html

📄 Sortie

Rapports dans reports/ : JSON + HTML.
⚖️ Licence

Usage éducatif et défensif uniquement.
👤 Auteur

@theanonspider — Cybersécurité éthique. 🐺
