import json
import random
import sys
import time

sys.path.append("/home/kalilinux_user/python_questions/Python/projects/Minecraft")
from woods import wood_data
from inventory.inventory import Inventory, Item


class ChopItems:
    def __init__(self, inventory):
        self.inventory = inventory

    def chop_items(self):
        # Extract wood quantities and chances
        wood_quantities = [wood.quantity for wood in wood_data]
        wood_chances = [wood.chances for wood in wood_data]

        # Get user input for number of woods to chop
        chop = int(input('How many woods you want to chop? '))

        # Check if the user has an axe in their inventory
        if any(item.name == 'axe' for item in self.inventory.items):
            print("Chopping wood...")

            # Simulate chopping wood
            time.sleep(2)  # Simulate time taken to chop wood

            # Determine the amount of wood obtained
            obtained_wood = random.choices(wood_quantities, wood_chances, k=chop)

            # Update inventory with obtained wood
            for wood in obtained_wood:
                self.inventory.add_item(Item(name='wood', quantity=wood))
            print(f"Obtained {sum(obtained_wood)} wood(s)")

        else:
            print("You need an axe to chop wood.")


# Example usage:
if __name__ == "__main__":
    # Initialize an inventory
    inventory = Inventory()

    # Initialize ChopItems with the inventory
    chop_items = ChopItems(inventory)
    chop_items.chop_items()

