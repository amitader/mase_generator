# Maze Generator and Solver

A Python application that visually generates and solves a maze using recursive backtracking and depth-first search (DFS). The maze is rendered using the Tkinter GUI library.

---

## 🧩 Features

- Procedural maze generation using recursive backtracking
- Visual maze solving using DFS
- Animated rendering via a custom `graphics.py` wrapper over Tkinter
- Fully interactive Tkinter window with step-by-step drawing
- Simple, modular codebase

## 🚀 How to Run

### Prerequisites

- Python 3.8+
- No external dependencies (uses only the standard library)

### Installation

Clone the repository:

```bash
git clone https://github.com/your-username/amitader-mase_generator.git
cd amitader-mase_generator
```
Run the project:

```bash
python main.py
```
The application will open a Tkinter window where the maze will be generated and solved in real time.


## 🛠️ Configuration
The default settings in main.py generate a 12x16 maze in an 800x600 window. You can tweak:

```python
num_rows = 12
num_cols = 16
screen_x = 800
screen_y = 600
margin = 50
```

## 📚 Code Overview
Cell class handles individual cell drawing and wall tracking.

Maze handles grid creation, wall breaking, and DFS solving.

Window, Point, Line (in graphics.py) abstract away Tkinter drawing.

main.py ties it all together with a configurable grid.

## 💡 Future Improvement Ideas
* Adding more solving algoritems

* A way to export maze to image or text

* Adding GUI buttons to control speed or re-generate

* Difficulty levels

