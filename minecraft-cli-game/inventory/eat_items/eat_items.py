import sys
import os
sys.path.append('/home/kalilinux_user/python_questions/Python/projects/Minecraft/inventory/eat_items')

from food_items import food_items_data
from inventory.inventory import Inventory, Item

class EatItem:
    def __init__(self, inventory):
        self.inventory = inventory
        self.food_items = {food_item.name: food_item for food_item in food_items_data}

    def eat_item(self, item_name):
        if item_name in self.food_items:
            food_item = self.food_items[item_name]
            if self.inventory.remove_item(item_name, 1):
                print(f"Ate one {item_name}. Replenished {food_item.fillhunger} hunger points.")
                return food_item.fillhunger
            else:
                print(f"{item_name} is not in the inventory.")
                return 0
        else:
            print(f"{item_name} is not a food item.")
            return 0

