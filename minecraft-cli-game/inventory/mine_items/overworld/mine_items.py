import random
import time
from blocks import blocks_data  # Importing blocks_data from blocks module
import sys
sys.path.append('/home/kalilinux_user/python_questions/Python/projects/Minecraft')
from inventory.inventory import Inventory, Item

class MineItems:
    def __init__(self, inventory):
        self.inventory = inventory
        self.blocks = {
            'above': [block for block in blocks_data if block.found_at in ['above','above_middle','all']],
            'middle': [block for block in blocks_data if block.found_at in ['middle','above_middle','middle_below','all']],
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
                    print(f"Can't mine at {max(valid_range)} (No Blocks found!!)")
                    return None
            except ValueError:
                print("Invalid input. Please enter an integer value.")

    def filter_blocks_by_level(self, y):
        if 0 <= y <= 80:
            return self.blocks['above']
        elif -48 <= y < 0:
            return self.blocks['middle']
        elif -58 <= y < -48:
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
        y = self.get_input("Which level do you want to mine? (between 80 and -58): ", range(80, -59, -1))
        if y is not None:
            blocks = self.get_input("How many blocks do you want to mine? (1-5): ", range(1, 6))
            if blocks is not None:
                print('')
                self.mine_items(y, blocks)


