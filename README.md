# 🔍 Recon-X

> **Boîte à outils OSINT automatisée pour l'analyse de surface d'attaque et la surveillance numérique.**
> Pour les tests de sécurité autorisés uniquement.

---

## 📖 Description

Recon-X est un outil de reconnaissance OSINT automatisé conçu pour les professionnels de la sécurité. Il collecte et analyse les informations publiquement disponibles sur une cible pour cartographier la surface d'attaque avant un test d'intrusion.

---

## ⚠️ Avertissement

**Cet outil est destiné à un usage autorisé uniquement.** Obtenez toujours une autorisation écrite avant d'analyser une cible.

---

## ⚙️ Installation

```bash
git clone https://github.com/theanonspider/Recon-X.git
cd Recon-X
pip install -r requirements.txt

🚀 Utilisation

bash
# Créer le token d'autorisation (obligatoire)
echo "RECON_X_AUTHORIZED" > reconx.token

# Lancer tous les modules
python reconx.py --target exemple.com

# Lancer un module spécifique
python reconx.py --target exemple.com --module domain_dns

# Dossier de sortie personnalisé
python reconx.py --target exemple.com --output ./resultats
🧩 Modules

Module	Description
domain_dns	Recherche WHOIS, résolution DNS, vérification SPF/DKIM/DMARC
subdomain_discovery	Scraping crt.sh + bruteforce de sous-domaines
port_scanning	Scan des ports courants + récupération de bannières
email_accounts	Génération de patterns d'emails + Have I Been Pwned
web_surface	Crawling léger, détection de panneaux d'administration, technologies
social_media	Recherche de profils sociaux (8 plateformes)
report	Génération de rapports JSON + HTML
📄 Sortie

text
output/
├── recon_exemple.com_20260730_143022.json   # Résultats complets
├── recon_exemple.com_20260730_143022.html   # Rapport HTML
🎨 Interface

Interface en ligne de commande stylée avec couleurs et barres de progression.

👤 Auteur

@theanonspider
