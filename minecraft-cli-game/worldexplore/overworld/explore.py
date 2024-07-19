import time
import sys
import os
sys.path.append('/home/kalilinux_user/python_questions/Python/projects/Minecraft')

from inventory.inventory import Inventory, Item
from inventory.eat_items.eat_items import EatItem

class OverExplore:
    def __init__(self, x=0, z=0, hunger=10):
        self.x = x
        self.z = z
        self.hunger = hunger
        self.inventory = Inventory()
        self.eat_items = EatItem(self.inventory)


    def display_hunger(self):

        full_hunger = "█" * int(self.hunger)
        empty_hunger = " " * (10 - int(self.hunger))
        print(f"\r[{full_hunger}{empty_hunger}] ({self.hunger:.1f}/10)",end="", flush=True)


    def eat(self):
        while self.hunger <= 0:
            food_item = input("\nWhat do you want to eat?")
            hunger_replenished = self.eat_items.eat_item(food_item)

            if hunger_replenished > 0:
                self.hunger += hunger_replenished
                print(f"Hunger_replenished by {hunger_replenished}.")
                self.display_hunger()

            else:
                print("Please choose a valid food item from inventory.")




    def movement(self, axis, blocks):
        print(f"Current position: ({self.x}, {self.z})")
        blocks_remaining = abs(blocks)
        direction = 1 if blocks > 0 else -1

        while blocks_remaining > 0:
            if self.hunger <= 0:
                print("\n Eat food to explore further.")
                self.eat()
                if self.hunger <= 0:
                    print("Player is too hungry to move")
                    break

            move_distance = min(3, blocks_remaining)
            if axis == 'x':
                self.x += direction * move_distance
            elif axis == 'z':
                self.z += direction * move_distance
            else:
                print(f"Invalid axis: {axis}. Please enter 'x' or 'z'.")
                return

            blocks_remaining -= move_distance
            self.hunger -= move_distance // 5
            print(f"\rPosition: ({self.x}, {self.z})",end='', flush=True)
            self.display_hunger()
            time.sleep(1)

        print(f"Final position: ({self.x}, {self.z})")


    def save_state(self):
        return {
        'x': self.x,
        'z': self.z,
        'hunger': self.hunger,
        'inventory': self.inventory.save_inventory()
        }

    def load_state(self, state):
        self.x = state['x']
        self.z = state['z']
        self.hunger = state['hunger']
        self.inventory.load_inventory(state['inventory'])


    def explore(self):
        try:
            axis = input("Enter the axis (x or z): ").lower()
            if axis not in ['x', 'z']:
                print("Invalid axis! Please enter 'x' or 'z'.")
                return

            blocks = int(input(f"How many blocks do you want to explore in {axis} axis? "))
            if blocks == 0:
                print("Player is not moving.")
                return

            self.movement(axis, blocks)

        except ValueError:
            print("Invalid input! Please enter an integer value for blocks.")
        except KeyboardInterrupt:
            print("\nExiting exploration.")

def main():
    explore = OverExplore()

    while True:
        explore.explore()

if __name__ == "__main__":
    main()
