## 🎮 Pygame Game Development

[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)](https://www.python.org/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)  
[![Made by Frank](https://img.shields.io/badge/Made%20by-FrankTheCodeBoy-blueviolet)](https://github.com/frankTheCodeBoy)

A modular 2D game built with Pygame, featuring alien enemies, animated characters, interactive buttons, and a scoring system. This project demonstrates object-oriented design, event handling, and game loop mechanics in Python.

---

### 🧩 Features

- 👾 Alien enemy logic (`aliens.py`)  
- 🔫 Bullet firing and collision detection (`game_bullets.py`)  
- 🧠 Game state management (`game_stats.py`)  
- 🕹️ Button interactions (`button.py`, `other_buttons.py`)  
- 🧮 Score tracking and high score persistence (`scoreboard.py`, `high_scores.json`)  
- ⚙️ Configurable settings (`settings.py`)  
- 🐉 Goku character module (`goku.py`)  
- 📸 Game assets in `game_pics/`

---

### 📁 Project Structure

```plaintext
PYGAME_GAME_DEVELOPMENT/
├── __pycache__/
├── game_pics/
├── aliens.py
├── button.py
├── game_bullets.py
├── game_load.py
├── game_stats.py
├── goku.py
├── other_buttons.py
├── scoreboard.py
├── settings.py
├── high_scores.json
├── instructions.txt
├── .gitignore
└── README.md
```

---

### 🚀 Getting Started

1. Clone the repo:
   ```bash
   git clone https://github.com/frankTheCodeBoy/PYGAME_GAME_DEVELOPMENT.git
   cd PYGAME_GAME_DEVELOPMENT
   ```

2. Install dependencies:
   ```bash
   pip install pygame
   ```

3. Run the game:
   ```bash
   python game_load.py
   ```

---

### 🎯 Purpose

This project was built to:

- Practice modular game development with Pygame  
- Explore object-oriented design in Python  
- Implement interactive UI elements and persistent scoring  
- Experiment with character animation and asset management

---

### 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

