# Maze-Explorer
This project, developed for the Introduction to Artificial Intelligence course, aims to present a maze-exploring model that uses different search methods to explore the environment. The proposal seeks[...] 

### 🧩 Maze Model

<pre style="font-size:16px; line-height:1.2em; font-family: monospace;">
<span style="color:gray;">###########</span>
<span style="color:gray;">#</span><span style="color:lime;">P</span>...<span style="color:gold;">E</span>....<span style="color:gray;">#</span>
<span style="color:gray;">#.#.#.###.#</span>
<span style="color:gray;">#.#.#...#.#</span>
<span style="color:gray;">#.#.###.#.#</span>
<span style="color:gray;">#...#</span><span style="color:red;">T</span><span style="color:gray;">#...#</span>
<span style="color:gray;">###.#.#.###</span>
<span style="color:gray;">#...#.#...#</span>
<span style="color:gray;">#.###.#.#.#</span>
<span style="color:gray;">#.....</span><span style="color:crimson;">I</span><span style="color:gray;">...#</span>
<span style="color:gray;">########</span><span style="color:deepskyblue;">X</span><span style="color:gray;">##</span>
</pre>


### 🗝️ Symbols

| Símbolo | Significado            |
|:--------:|------------------------|
| `#`      | Wall                   |
| `P`      | Player (initial point) |
| `X`      | Finish (goal)          |
| `T`      | Trap                   |
| `E`      | Enemy                  |
| `I`      | Point / Item to colect |
| `.`      | Empty space / way      |

## Requirements and How to run Main

Requirements
- Python 3.8 or newer (recommended).
- pip (Python package manager).
- (Optional) virtual environment (venv or virtualenv) to isolate dependencies.

Installation (optional)
1. Clone the repository and change to the project folder:
   - git clone https://github.com/cauabrasil25/Maze-Explorer.git
   - cd Maze-Explorer
2. Create and activate a virtual environment:
   - Linux / macOS:
     - python3 -m venv .venv
     - source .venv/bin/activate
   - Windows (PowerShell):
     - python -m venv .venv
     - .\.venv\Scripts\Activate.ps1
3. If a requirements.txt file exists, install dependencies:
   - pip install -r requirements.txt

How to run the Main
- From the repository root run:
  - python3 src/Main.py
  - On Windows you can also use: py -3 src/Main.py
- If you encounter import errors, run as a module from the repo root:
  - python -m src.Main

Notes
- Make sure you run the command from the project root so that relative imports work correctly.
- If a missing package error occurs, install the missing package with pip or check for a requirements.txt file.
- Using a virtual environment is recommended for development to avoid global package conflicts.