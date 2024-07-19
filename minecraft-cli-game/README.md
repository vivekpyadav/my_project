# Minecraft CLI Game

Welcome to the Minecraft CLI Game, a text-based adventure inspired by the popular game Minecraft. Explore, mine, craft, and manage your inventory as you navigate through a blocky world, all from the command line.

## Features

- **Explore:** Move around the world on the x and z axes.
- **Mine:** Dig for resources at different levels.
- **Craft:** Combine items to create new tools and objects (in progress..).
- **Smelt:** Convert raw materials into usable items (coming soon).
- **Store:** Organize and store your items (coming soon).
- **Throw:** Discard unwanted items (coming soon).
- **Breed:** Breed animals for resources (coming soon).
- **Collect:** Collect resources by killing entities (coming soon).
- **Eat:** Consume food to restore hunger.
- **Cook:** Prepare food items (coming soon).
- **Sleep:** Sleep to skip the night (coming soon).
- **Save and Quit:** Save your progress and exit the game.

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/vivekpyadav/my_project/tree/main/minecraft-cli-game
    cd minecraft-cli-game
    ```

2. **Ensure you have Python installed (version 3.6 or higher).**

3. **Run the game:**
    ```sh
    python main_menu.py
    ```

## Usage

When you start the game, you'll be presented with a menu of options to choose from. Enter the corresponding command to perform an action.

### Commands

- `explore`: Move around the world.
  - Enter the axis (`x` or `z`) and the number of blocks to move.
- `mine`: Dig for resources.
  - Enter the level to mine (between 80 and -58) and the number of blocks (1-5).
- `craft`, `smelt`, `store`, `throw`, `breed`, `collect`, `eat`, `cook`, `sleep`: Perform respective actions (some features are coming soon).
- `quit`: Save your progress and exit the game.

## Example Gameplay

```plaintext
+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
| Welcome to your new World(;P) |
+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+

    o---------------------------o
    | Explore:------(explore)   |
    | Mine items:---(mine)      |
    | Show mined:---(show mined)|
    | Craft items:--(craft)     |
    | Smelt items:--(smelt)     |
    | Store items:--(store)     |
    | Throw items:--(throw)     |
    |- - - - - - - - - - - - -  |
    | Breeding:-----(breed)     |
    | kill:---------(collect)   |
    |- - - - - - - - - - - - -  |
    | Eat items:----(eat)       |
    | Cook items:---(cook)      |
    |- - - - - - - - - - - - -  |
    | Sleep:--------(sleep)     |
    | Save and quit:(quit)      |
    o---------------------------o

Coordinates: x=0, z=0
Hunger bar: 10.0/10
Current Inventory:

Enter your choice: mine
Which level do you want to mine? (between 80 and -58): 45
How many blocks do you want to mine? (1-5): 4

Found a copper! Mined in 3 seconds.
Found a coal! Mined in 3 seconds.
Found a gravel! Mined in 2 seconds.
Found a stone! Mined in 1 seconds.

Enter your choice: quit

