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

# Créer le token d'autorisation (obligatoire)
echo "RECON_X_AUTHORIZED" > reconx.token

# Lancer
python reconx.py --target exemple.com

🧩 Modules

Domaine & DNS
Découverte de sous-domaines
Scan de ports
Emails & Comptes
Surface web
Réseaux sociaux & Médias
Génération de rapports

👤 Auteur

@theanonspider
