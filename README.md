# 🕷️ Spider-VMAX (Private)

> **Advanced Command & Control framework — Malleable C2, Polymorphic, Undetectable.**
> Private version — Do not distribute.

---

## 📊 Statistics

| Element | Count |
|---------|-------|
| Modules | 18 |
| Interface | Web Dashboard + WebSockets |
| C2 Protocols | HTTP/HTTPS, DNS, P2P |
| Encryption | AES-256 |
| Total files | 22 |

---

## 🧩 Modules

### Core
- **Server** — Flask dashboard + WebSocket API
- **Agent** — Multi-OS client (Windows/Linux/macOS)
- **Crypto** — AES-256 encryption
- **Persistence** — Windows/Linux/macOS
- **SysInfo** — System information collection
- **Screenshot** — Screen capture
- **Keylogger** — Keyboard input capture
- **Shell** — Remote command execution
- **File Manager** — Upload/download files
- **Anti-VM** — VM detection
- **Anti-Debug** — Debugger detection

### Advanced
- **DNS Tunnel** — C2 over DNS queries
- **P2P** — Peer-to-peer agent communication
- **Polymorphic** — Unique agent builds
- **Spread** — Network propagation (SMB)
- **Malleable C2** — Traffic obfuscation (jQuery, Google Analytics, Slack, CDN)
- **Sleep Obfuscation** — Memory evasion (Ekko, Foliage)
- **WebSocket Server** — Real-time dashboard

---

## ⚙️ Installation

```bash
git clone [PRIVATE_URL]
cd Spider-VMAX
pip install -r requirements.txt

🚀 Usage

bash
# Token required
echo "SPIDER_C2_AUTHORIZED" > spiderc2.token

# Start server
python spidervmax.py server

# Generate agent
python spidervmax.py generate --type windows

# Network scan
python spidervmax.py scan --target 192.168.1
🎨 Web Dashboard

URL: http://localhost:8080
Login: admin / SpiderVMAX-2024!
Real-time updates via WebSockets
Live console, agent map, command center
🆚 vs Cobalt Strike

Cobalt Strike	Spider-VMAX
Modules	~10	18
Malleable C2	✅	✅
Sleep Obfuscation	✅	✅
Polymorphic	❌	✅
Anti-VM	❌	✅
Anti-Debug	❌	✅
WebSockets	❌	✅
Price	€40k/yr	Free
⚠️ Warning

Private project. Do not distribute.
Educational use only in isolated environments.
---

