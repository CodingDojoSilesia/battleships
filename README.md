# Goal of assignment

BATTLESHIPS / STATKI

Make a retro game in retro style :) 
Rules in English: https://en.wikipedia.org/wiki/Battleships_game
Rules in Polish: https://pl.wikipedia.org/wiki/Okr%C4%99ty

# Prerequisites

* Python 3
* virtual environment
* Linux/Mac require glfw or libglfw depending on OS

# How to start

* clone this repo
* make virtual environment
* install dependencies from `requirements.txt`
* run `python game.py`

# Files

* `base.py` has a 'core' of game used in `game.py`
* `tests.py` has two tests as examples
* `tile.png` images :3
* `README.md` this file
* `requirements.txt` - requirements to install by pip
* `game.py` is a main program (to edit by you.) with 4 necessary methods:

1. `__init__` - only to init attributes in this class
2. `setup` - will be invoked before start of game (ex. init ships)
3. `tick` - in this method we can implement any actions (like mouse click or sth)
4. `draw_game` - in this method we can draw text and images


# Goals
## Must to have

* Make two boards (Player and Enemy [Hidden])
* add ships to boards (2×3, 3×2, 4×1) (placement might be randomized),
remember about 1-cell margin beetwen ships!
* Dummy AI - random()
* Turns, Attacking! (based on rules)

## Fancy optional

* TDD OMG!
* Ships placement before start
* AI!!!
