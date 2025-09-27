<!-- Pongfinity — Styled README -->

<p align="center">
  <img alt="Pongfinity logo" src="https://img.shields.io/badge/Pongfinity-%F0%9F%8E%AE-blue" />
</p>

# 🎮 Pongfinity — A Ping‑Pong Game

**Pongfinity** is a lightweight, desktop Pong-inspired arcade game built with **Python + Pygame**. Play single‑player or local two‑player, keep highscores, and package it into a distributable executable.

---

## 🔖 Quick links

* **Source:** `https://github.com/Aashishst/Pongfinity-A-ping-Pong-Game`
* **Run locally:** `python Aashish-K_Pongfinity.py`
* **Build (Windows):** PyInstaller `--onefile --windowed`

---

## ✨ Features

* Classic Pong gameplay with smooth paddle & ball physics
* Two modes: **Single Player** (bottom paddle) and **Local Multiplayer** (two paddles)
* Persistent scores & highscores (plain text files)
* Pause / Resume, Restart, and Quit controls
* Single-file script — easy to run and package

---

## 📁 Project structure

```
Pongfinity-A-ping-Pong-Game/
├─ Aashish-K_Pongfinity.py      # main script
├─ README.md                    # this file
├─ (optional) S_score.txt       # single player last score
├─ (optional) S_highscore.txt
├─ (optional) O_score.txt       # multiplayer opponent score files
└─ (optional) O_highscore.txt
```

> Scores are saved in the script directory. Deleting those files resets highscores.

---

## 🛠️ Prerequisites

* Python 3.8+
* Pygame

Install Pygame:

```bash
pip install pygame
```

---

## Run locally

- There are two ways to do this. Both are shown below.

### Method 1:

1. Go to the repo
     
2. Open the Python folder

3.  Download a file(In a premade folder **(Recommended)**)
'
### Method 2

1. Clone the repo:

```bash
git clone https://github.com/Aashishst/Pongfinity-A-ping-Pong-Game.git
cd Pongfinity-A-ping-Pong-Game
```

2. (Recommended) create a virtualenv and activate it
3. Install dependencies and run:

```bash
pip install -r requirements.txt   # or pip install pygame
python Aashish-K_Pongfinity.py
```

---

## ⌨️ Controls

* **Multiplayer:**

  * Player 1: `W` (up), `S` (down)
  * Player 2: `↑` / `↓` (up/down)
* **Single Player:** `←` / `→` to move paddle
* **Global:** `Q` to quit (or close window)

---

## 📦 Packaging into an executable

Build on the target OS (Windows → Windows, Linux → Linux).

**Windows example (PyInstaller):**

```bash
pip install pyinstaller
pyinstaller --onefile --windowed Aashish-K_Pongfinity.py
```

* Result: `dist/Aashish-K_Pongfinity.exe` (zip it and upload to Releases or itch.io)
* If you add assets later, include with `--add-data "assets;assets"` (Windows) or `--add-data "assets:assets"` (Linux/macOS).

---

## 🧩 Asset & packaging tips

* The script currently uses plain-text highscores and system fonts — bundle a `.ttf` for consistent typography across systems.
* When adding images/sounds, use the helper below to load files reliably (works with PyInstaller):

```python
import sys, os

def resource_path(relative_path):
    if getattr(sys, 'frozen', False):
        base = sys._MEIPASS
    else:
        base = os.path.abspath('.')
    return os.path.join(base, relative_path)
```

---

## ⚠️ Troubleshooting

* **404 on GitHub Pages:** Pages needs an `index.html` — GitHub Pages can't run Pygame.
* **Missing score files:** The game auto-creates them; delete to reset.
* **Black window / no display:** Ensure Pygame installed and a display server (X/Wayland) is available on Linux.
* **AV flags on exe:** New binaries can trigger false positives; sign binaries or inform users.

---

## 🤝 Contributing

Contributions welcome! Fork → branch → PR. Suggested improvements:

* Add music & sfx
* Add difficulty settings and an options menu
* Add keyboard remapping and fullscreen toggle

---


*Want this committed to your repo or want a GitHub Pages `index.html` created with this README excerpt? Tell me and I’ll do it for you.*
