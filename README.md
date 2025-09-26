# Pongfinity — A Ping Pong Game

**Short description**
Pongfinity is a lightweight, desktop Ping‑Pong (Pong) game built with Pygame. It focuses on classic arcade gameplay with crisp controls. This project was made with AI though only for a some physics and unknown pygame topics which I could not covee.

---

## Features

* Classic Pong gameplay (paddles, ball physics, scoring).
* Two-player local mode (keyboard) and single-player mode vs AI (if implemented).
* Pause / Resume and Restart functionality.
* Sound effects and music support (assets in `assets/`).
* Keeps score and displays a game-over/winner screen.
* Asset-friendly: graphics and sounds loaded from `assets/` folder so you can swap or mod them easily.
* Easy packaging for distribution using **PyInstaller**.

> *If any feature below doesn’t match your repo, tell me and I’ll update the README to exactly reflect the project.*

---

## Prerequisites

* Python 3.8+ installed
* `pip` available
* (Optional) Virtual environment recommended

---

## Install & Run (local)

1. Clone the repo:

```bash
git clone https://github.com/aashishst/Pongfinity-A-ping-Pong-Game.git
cd Pongfinity-A-ping-Pong-Game
```

2. Create and activate a virtual environment (recommended)

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
# or simply
pip install pygame
```

4. Run the game:

```bash
python Aashish-K_Pongfinity.py
```

---

## Controls (common layout)

* **Player 1:** `W` (up), `S` (down)
* **Player 2:** `Up Arrow`, `Down Arrow`
* **Quit:** `Q` or window close

*Adjust keys in the script if you prefer different bindings.*

---


## Releases & GitHub Pages

* Upload built ZIP/exe to **Releases** in GitHub for easy downloads.
* GitHub Pages can host a project page (`index.html`) describing the game, but cannot run Pygame in the browser.

---

## Contribution

Contributions welcome:

* Fork the repo, create a feature branch, open a pull request. Please include a short description and reproducible steps for bugs.

