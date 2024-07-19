import os
import json
import time
import sys

# Ensure these paths are correct based on your project structure
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'inventory/mine_items/overworld')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'inventory')))

from inventory.inventory import Inventory, Item
from inventory.eat_items.eat_items import EatItem
from worldexplore.overworld.explore import OverExplore
from inventory.mine_items.overworld.mine_items import MineItems  # Ensure correct path to MineItems

def display_world_menu():
    print("+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+")
    print("| Welcome to your new World(;P) |")
    print("+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+\n")

    print("""
    o--------------------------o
    | Explore:------(explore)  |
    | Mine items:---(mine)     |
    | Craft items:--(craft)    |
    | Smelt items:--(smelt)    |
    | Store items:--(store)    |
    | Throw items:--(throw)    |
    |- - - - - - - - - - - - - |
    | Breeding:-----(breed)    |
    | kill:---------(collect)  |
    |- - - - - - - - - - - - - |
    | Eat items:----(eat)      |
    | Cook items:---(cook)     |
    |- - - - - - - - - - - - - |
    | Sleep:--------(sleep)    |
    | Save and quit:(quit)     |
    o--------------------------o

    \n""")

def display_hunger(hunger):
    print(f"Hunger bar: {hunger:.1f}/10")

def display_inventory(inventory):
    print("Current Inventory:")
    inventory.show_inventory()

def display_coordinates(coordinates):
    print(f"Coordinates: x={coordinates['x']}, z={coordinates['z']}")

def eat(inventory, world_state):
    eat_items = EatItem(inventory)  # Initialize EatItem instance with inventory

    while True:
        food_item = input("What do you want to eat? ").strip().lower()

        if food_item == "exit":
            break

        hunger_replenished = eat_items.eat_item(food_item)

        if hunger_replenished > 0:
            world_state['hunger'] = min(world_state['hunger'] + hunger_replenished, 10)
            print(f"Hunger replenished by {hunger_replenished}.")
            display_hunger(world_state['hunger'])
        else:
            print(f"Could not replenish hunger with {food_item}.")

def cook():
    # Placeholder for cooking functionality
    print("Cooking items coming soon!")

def dict_to_inventory(data):
    inventory = Inventory()
    inventory.load_inventory(data)
    return inventory

def inventory_to_dict(inventory):
    print(f"Converting inventory to dict: {inventory}")
    return inventory.save_inventory()




def save_world(world_state, world_name):

    filename = f'saves/{world_name}.json'
    with open(filename, 'w') as f:
        json.dump(world_state, f, indent=4)
    print(f"World saved to {filename}")

def load_world(world_name):
    file_path = os.path.join("saves", world_name + ".json")
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            world_state = json.load(file)
        print(f"Inventory loaded from: {file_path}")
        
        if isinstance(world_state['inventory'], dict):
            world_state['inventory'] = dict_to_inventory(world_state['inventory'])
        return world_state
    else:
        print(f"No saved world found with the name: {world_name}")
        return None

def main(world_name, world_state):
    coordinates = world_state.get("coordinates", {"x": 0, "z": 0})
    hunger = world_state.get("hunger", 10)
    inventory = world_state.get("inventory")
    if isinstance(inventory, dict):
        inventory = dict_to_inventory(inventory)

    miner = MineItems(inventory)  # Initialize MineItems with the inventory

    display_world_menu()
    display_coordinates(coordinates)
    display_hunger(hunger)
    display_inventory(inventory)

    while True:
        try:
            option = input("Enter your choice: ").strip().lower()

            if option == "explore":
                axis = input("Enter the axis (x or z): ").strip().lower()
                blocks = int(input(f"How many blocks do you want to explore in {axis} axis? ").strip())

                if axis in coordinates:
                    for i in range(1, blocks + 1):
                        time.sleep(0.5)  # Simulate travel time
                        coordinates[axis] += 1
                        hunger -= 0.2  # Reduce hunger gradually
                        hunger = max(hunger, 0)  # Ensure hunger doesn't go below 0
                        hunger_bar = "█" * int(hunger) + " " * (10 - int(hunger))
                        print(f"\rTraveling... Coordinates: ({coordinates['x']}, {coordinates['z']}) Hunger: [{hunger_bar}] ({hunger:.1f}/10)", end="")
                        if hunger <= 0:
                            print("\nYou are too hungry to continue exploring. Eat something!")
                            break
                    print(f"\nFinal position: ({coordinates['x']}, {coordinates['z']})")
                    print(f"Hunger bar: [{hunger}] ({hunger:.1f}/10)")
                else:
                    print("Invalid axis. Please choose either 'x' or 'z'.")

            elif option == "mine":
                miner.mine_level()  # Call mine_level method
                print("")
                inventory.show_inventory()


            elif option == "craft":
                # Implement crafting functionality
                print("Crafting items coming soon!")
            elif option == "smelt":
                # Implement smelting functionality
                print("Smelting items coming soon!")
            elif option == "store":
                # Implement storing functionality
                print("Storing items coming soon!")
            elif option == "throw":
                # Implement throwing functionality
                print("Throwing items coming soon!")
            elif option == "breed":
                # Implement breeding functionality
                print("Breeding coming soon!")
            elif option == "collect":
                # Implement killing/collecting functionality
                print("Killing/collecting items coming soon!")
            elif option == "eat":
                eat(inventory, world_state)
            elif option == "cook":
                cook()
            elif option == "sleep":
                # Implement sleeping functionality
                print("Sleeping coming soon!")
            elif option == "quit":
                world_state['coordinates'] = coordinates
                world_state['hunger'] = hunger
                print(f"Inventory before conversion: {inventory}")
                world_state['inventory'] = inventory_to_dict(inventory)  # Convert inventory to dictionary before saving
                save_world(world_state, world_name)
                print("Saving and quitting the game...")
                break
            else:
                print("Invalid option. Please select a valid choice.")

            world_state['coordinates'] = coordinates
            world_state['hunger'] = hunger
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    import sys
    import os

    if not os.path.exists("saves"):
        os.makedirs("saves")

    if len(sys.argv) < 2:
        print("Usage: main_menu1.py <world_name>")
        sys.exit(1)

    world_name = sys.argv[1]

    filename = f"saves/{world_name}.json"
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            world_state = json.load(f)
        inventory_data = world_state.get("inventory", {})
        world_state["inventory"] = dict_to_inventory(inventory_data)
    else:
        world_state = {
            "coordinates": {"x": 0, "z": 0},
            "hunger": 10,
            "inventory": Inventory()
        }

    main(world_name, world_state)







