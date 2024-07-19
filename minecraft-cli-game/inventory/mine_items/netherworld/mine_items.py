import random
import time
import sys
sys.path.append('/home/kalilinux_user/python_questions/Python/projects/Minecraft')
from blocks import blocks_data  # Importing blocks_data from blocks module
from inventory.inventory import Inventory, Item

class MineItems:
    def __init__(self, inventory):
        self.inventory = inventory
        self.blocks = {
            'above': [block for block in blocks_data if block.found_at in ['all']],
            'middle': [block for block in blocks_data if block.found_at in ['middle','middle_below','all']],
            'below': [block for block in blocks_data if block.found_at in ['below','middle_below','all']]
        }

    def get_input(self, prompt, valid_range):
        while True:
            try:
                value = int(input(prompt))
                if value in valid_range:
                    return value
                elif value < min(valid_range):
                    print(f"Can't mine at {min(valid_range)} (BEDROCK Found!!)")
                    return None
                elif value > max(valid_range):
                    print(f"Can't mine at {max(valid_range)} (BEDROCK Found!!)")
                    return None
            except ValueError:
                print("Invalid input. Please enter an integer value.")

    def filter_blocks_by_level(self, y):
        if 70 <= y <= 124:
            return self.blocks['above']
        elif 18 <= y < 70:
            return self.blocks['middle']
        elif 2 <= y < 18:
            return self.blocks['below']
        else:
            return []

    def mine_items(self, y, blocks):
        block_list = self.filter_blocks_by_level(y)
        if not block_list:
            print("No suitable blocks found at this level.")
            return

        block_names = [block.name for block in block_list]
        block_weights = [block.priority for block in block_list]

        result = random.choices(block_list, weights=block_weights, k=blocks)
        for block in result:
            time.sleep(block.mining_speed)
            print(f"Found a {block.name}! Mined in {block.mining_speed} seconds.")
            self.inventory.add_item(Item(block.name), 1)

    def mine_level(self):
        print('')
        y = self.get_input("Which level do you want to mine? (between 124 and 2 ): ", range(124, 2, -1))
        if y is not None:
            blocks = self.get_input("How many blocks do you want to mine? (1-5): ", range(1, 6))
            if blocks is not None:
                print('')
                self.mine_items(y, blocks)

if __name__ == "__main__":
    inventory = Inventory()
    miner = MineItems(inventory)
    while True:
        print("""
                1. Mine
                2. Show Inventory
                3. Exit
              """)
        choice = input("Enter your choice: ")
        if choice == '1':
            miner.mine_level()
        elif choice == '2':
            inventory.show_inventory()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")







