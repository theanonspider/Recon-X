# 🔍 Recon-X

> **Automated OSINT toolkit for attack surface analysis and digital surveillance.**
> For authorized security testing only.

---

## 📖 Description

Recon-X is an automated OSINT reconnaissance tool designed for security professionals. It collects and analyzes publicly available information about a target domain to map the attack surface before a penetration test.

---

## ⚠️ Warning

**This tool is for authorized use only.** Always obtain written permission before scanning any target.

---

## ⚙️ Installation

```bash
git clone https://github.com/theanonspider/Recon-X.git
cd Recon-X
pip install -r requirements.txt

🚀 Usage

bash
# Create authorization token (required)
echo "RECON_X_AUTHORIZED" > reconx.token

# Run all modules
python reconx.py --target example.com

# Run specific module
python reconx.py --target example.com --module domain_dns

# Custom output directory
python reconx.py --target example.com --output ./results

🧩 Modules

Module	Description
domain_dns	WHOIS lookup, DNS resolution, SPF/DKIM/DMARC checks
subdomain_discovery	crt.sh scraping + subdomain bruteforce
port_scanning	Common port scanning + banner grabbing
email_accounts	Email pattern generation + Have I Been Pwned
web_surface	Light crawling, admin panel detection, tech fingerprinting
social_media	Social media profile search (8 platforms)
report	JSON + HTML report generation
📄 Output

text
output/
├── recon_example.com_20260730_143022.json   # Full results
├── recon_example.com_20260730_143022.html   # HTML report
🎨 CLI

Styled command-line interface with colors and progress bars.

👤 Author

@theanonspider
