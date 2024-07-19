import sys
sys.path.append("/home/kalilinux_user/python_questions/Python/projects/Minecraft")
from inventory.inventory import Inventory, Item
import json
import os

class MainMenu:
    def __init__(self):
        self.directory = "saves/" 

    def create_new_world(self):
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)

        worldname = input("Enter the name of your world: ")
        file_path = os.path.join(self.directory, worldname + '.json')

        if os.path.exists(file_path):
            print(f"World {worldname} already exists!")
            return None

        world_state = {
            "world_name": worldname,
            "coordinates": {"x": 0, "z": 0},
            "hunger": 10,
            "inventory": {}
        }

        with open(file_path, 'w') as file:
            json.dump(world_state, file)
            print(f"--=Created a New world ({worldname})=--")

    def delete_world(self):
        worldname = input("Enter the world to delete: ")
        file_path = os.path.join(self.directory, worldname + '.json')

        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"World ({worldname}) deleted successfully.")
        else:
            print(f"World ({worldname}) does not exist.")

    def display_saved_worlds(self):
        if not os.path.exists(self.directory):
            print("No saved worlds found.")
        else:
            worlds = os.listdir(self.directory)
            if worlds:
                print("Saved Worlds:")
                for world in worlds:
                    worldname = os.path.splitext(world)[0]
                    length = len(worldname)
                    print((length + 2) * "-")
                    print(f"|{worldname}|")
                    print((length + 2) * "-", end="   <-----")
            else:
                print("No saved worlds found.")

    def load_inventory(self):
        worldname = input("Enter the name of Saved World: ")
        file_path = os.path.join("saves", worldname + ".json")

        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                world_state = json.load(file)

            print(f"Inventory loaded from: {file_path}\n")
            return world_state
        else:
            print(f"No saved inventory found for {worldname}")
            return None

def display_main_menu():
    print("[---------==M I N E C R A F T ==---------]\n\n")
    print('+========================================+')
    print('|         Start the game-(start)         |')
    print('+----------------------------------------+')
    print('|            Quit game-(quit)            |')
    print('+========================================+\n')

def main_menu():
    menu = MainMenu()
    while True:
        display_main_menu()
        choice = input("/")
        print('')
        print("")
        try:
            if choice == 'start':
                while True:
                    menu.display_saved_worlds()
                    print('')
                    print("\n+---------+")
                    print('|[OPTIONS]|')
                    print("+---------+----------------------+")
                    print("| Create a New World! - (create) |")
                    print("| Load World! - (load)           |")
                    print('| Delete World! - (delete)       |')
                    print("| << Go back - (back)            |")
                    print("+--------------------------------+\n")

                    option = input("/")
                    try:
                        if option == "create":
                            menu.create_new_world()
                            print("")
                        elif option == "load":
                            world_state = menu.load_inventory()
                            if world_state:
                                import ingame
                                ingame.main(world_state.get('world_name', 'unknown'), world_state)
                            print("")
                        elif option == "delete":
                            menu.delete_world()
                            print("")
                        elif option == "back":
                            print("")
                            break
                        else:
                            print("Invalid option selected")
                            print("")
                    except Exception as e:
                        print(f"An error occurred: {e}")
            elif choice == "quit":
                print("Quitting game!")
                break
            else:
                print("Invalid choice!")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main_menu()

