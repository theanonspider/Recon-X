# 🔍 RECON-X V1 — DOCUMENTATION OFFICIELLE

> **Boîte à outils OSINT automatisée pour l'analyse de surface d'attaque et la surveillance numérique.**
> Version publique — Open Source — Usage éducatif

---

## 📊 FICHE TECHNIQUE

| Élément | Détail |
|---------|--------|
| **Nom** | Recon-X |
| **Version** | 1.0 (Publique) |
| **Type** | Outil OSINT automatisé |
| **Licence** | MIT (usage éducatif uniquement) |
| **Langage** | Python 3 |
| **Plateforme** | Multi-plateforme (Windows, Linux, macOS) |
| **Interface** | CLI stylée (rich) |
| **Modules** | 7 |
| **Dépôt** | github.com/theanonspider/Recon-X |

---

## 🧩 MODULES

### 🌐 Domaine & DNS
- WHOIS (registrar, dates, serveurs de noms)
- Résolution DNS (A, AAAA, MX, NS, TXT, CNAME)
- Vérification SPF, DKIM, DMARC

### 🔍 Découverte de sous-domaines
- Scraping Certificate Transparency (crt.sh)
- Bruteforce intelligent (21 préfixes courants)

### 📡 Scan de ports
- 17 ports communs (FTP, SSH, HTTP, HTTPS, RDP, MySQL, etc.)
- Récupération de bannières de services

### 📧 Emails & Comptes
- Génération de patterns d'emails (contact, info, admin, etc.)
- Vérification Have I Been Pwned

### 🕸️ Surface web
- Crawling léger (robots.txt, sitemap.xml, login, admin)
- Détection de panneaux d'administration
- Détection de technologies (WordPress, Joomla, Drupal)

### 👥 Réseaux sociaux
- Recherche de profils sur 8 plateformes
- Facebook, Twitter/X, Instagram, LinkedIn, YouTube, GitHub, TikTok, Reddit

### 📊 Rapports
- Génération JSON
- Génération HTML stylé

---

## 🔐 SÉCURITÉ

| Mécanisme | Description |
|-----------|-------------|
| **Token d'autorisation** | Fichier `reconx.token` obligatoire |
| **Code source ouvert** | Vérifiable par tous |

---

## ⚙️ INSTALLATION

```bash
git clone https://github.com/theanonspider/Recon-X.git
cd Recon-X
pip install -r requirements.txt

🚀 UTILISATION

bash
# Token obligatoire
echo "RECON_X_AUTHORIZED" > reconx.token

# Tous les modules
python reconx.py --target exemple.com

# Module spécifique
python reconx.py --target exemple.com --module domain_dns

# Sortie personnalisée
python reconx.py --target exemple.com --output ./resultats
📄 SORTIE

recon_*.json : résultats complets
recon_*.html : rapport HTML stylé
⚠️ AVERTISSEMENT

Cet outil est fourni à des fins exclusivement éducatives et défensives.
Toute utilisation sur une cible sans autorisation écrite est ILLÉGALE.

👤 AUTEUR

@theanonspider — Cybersécurité éthique

Document généré le 30 juillet 2026
