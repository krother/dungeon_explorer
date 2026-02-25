# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repository Is

This is a **Python tutorial project** — a step-by-step course teaching beginners how to build a 2D dungeon crawler game. The repository has two distinct parts:

1. **The game itself** (in the folder `solution/`) — a working 2D game using OpenCV for rendering
2. **The tutorial documentation** (`chapters/`, `index.rst`) — a Sphinx-based book walking students through building the game feature by feature

## Build and Run Commands

Install dependencies (use `uv`):
```bash
python -m pip install uv
uv sync
```

Build the Sphinx HTML documentation:
```bash
uv run make html
```

The built docs go into `build/html/`.

## Architecture

### Game Code

The main files of the game are:

- **[game.py](game.py)** — Pure game logic with no I/O. Uses `pydantic` `BaseModel` for all data structures (`DungeonGame`, `Level`, `Teleporter`, `Fireball`, `Skeleton`). Contains level definitions (`LEVEL_ONE`, `LEVEL_TWO`) as string-grid maps encoded with single characters (`.` floor, `#` wall, `€` coin, `T` trap, `k` key, `x` stairs, `D`/`d` closed/open door, `~` slime). Functions: `start_game()`, `move_player()`, `update()`, `check_teleporters()`, `check_collision()`.

- **[main.py](main.py)** — Graphics engine using OpenCV (`cv2`) + NumPy. Reads PNG tile images from `tiles/`, renders the dungeon grid at 64px per tile, handles keyboard input (WASD keys), and runs the main game loop. The `SYMBOLS` dict maps map characters to tile image names.

- The map grid is a `list[list[str]]` of single characters — each character is both the tile type identifier and what gets stored in the level data
- Game state is entirely in the `DungeonGame` pydantic model — no global mutable state in `game.py`
- `main.py` is intentionally simple and tutorial-friendly — it runs as a top-level script (no `if __name__ == "__main__"` guard)
- The tutorial is intended for Python beginners; keep game code readable and avoid advanced abstractions
- pydantic classes are used as data structures only. Not methods. All behavior is defined in toplevel functions.

### Tutorial Structure

Each chapter in `chapters/` corresponds to one feature added to the game. The `solution/` directory contains numbered snapshots of the game at each tutorial step (e.g., `solution/001_floor/`, `solution/002_walls/`), each containing a `game.py` and `main.py` at that stage. The `prototype/` directory contains the starting code students begin with.

- Sphinx config is given in `conf.py`
- Images: `images/` for doc images, `tiles/` for game tile PNGs, `_static/` for CSS/logo

