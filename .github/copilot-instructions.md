# Copilot Instructions for PROJET-CASSE-BRIQUE

## Project Overview
This is a Python implementation of a classic brick-breaker (casse-brique) game. The codebase is organized into several key modules:
- `balle.py`: Ball logic and movement
- `cases.py`: Brick/case management
- `UI.py`: User interface and game loop
- `FILE1.py`: (Purpose unclear, review before major changes)

## Architecture & Data Flow
- The game logic is split between ball movement (`balle.py`), brick/case state (`cases.py`), and UI/game loop (`UI.py`).
- UI interacts with ball and cases modules to update game state and render changes.
- No external dependencies detected; pure Python.

## Developer Workflows
- **Run the game:** Launch via `UI.py` (likely entry point)
- **Debugging:** Add print statements or use Python's built-in debugger (`pdb`).
- **Testing:** No formal test suite detected; manual testing via running the game is expected.

## Project-Specific Patterns
- Each major game component is separated into its own file for clarity.
- Game state is likely managed via classes or global variables in each module.
- UI code may directly manipulate objects from `balle.py` and `cases.py`.

## Conventions
- File names are lowercase and descriptive of their purpose.
- No type hints or docstrings detected; follow existing style unless refactoring.
- No requirements.txt or setup.py; assume no external packages.

## Integration Points
- All logic appears internal; no API calls or external services.
- If adding features, keep new logic modular and place in a new file if it doesn't fit existing ones.

## Examples
- To add a new power-up, create a new file (e.g., `powerup.py`) and integrate with `UI.py`.
- To change ball physics, edit `balle.py` and ensure UI updates reflect changes.

## Key Files
- `UI.py`: Main loop and user interaction
- `balle.py`: Ball movement and collision
- `cases.py`: Brick/case state

---
**If any section is unclear or missing, please provide feedback so this guide can be improved.**
