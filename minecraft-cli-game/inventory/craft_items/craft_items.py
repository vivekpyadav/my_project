from recipes import recipes
from inventory.inventory import Inventory

my_list = [['', '', ''], ['', '', ''], ['', '', '']]
inventory = Inventory()

def display_crafting_table():
    horizontal_line = "+---+---+---+"
    for row in my_list:
        print(horizontal_line)
        print("|" + "|".join(f" {item[0] if item else ' '} " for item in row) + "|")
    print(horizontal_line)


def check_crafting_table(inventory):
    for recipe_name, recipe_data in recipes.items():
        recipe = recipe_data["recipe"]
        result = recipe_data["result"]

        print(f"Checking recipe: {recipe_name}")

        match = True
        required_items = {}
        for i in range(3):
            for j in range(3):
                if recipe[i][j]:
                    if my_list[i][j] != recipe[i][j]:
                        match = False
                        break
                    else:
                        required_items[recipe[i][j]] = required_items.get(recipe[i][j], 0) + 1
            if not match:
                break

        if match:
            if inventory.use_items(required_items):
                print(f"You have crafted {result}!")
                # Clear the crafting table after crafting
                return
            else:
                print(f"Not enough items in inventory to craft {result}.")
                return

    print("No valid recipe matched.")



def craft(inventory):
    for i in range(1, 10):
        item_insert = input(f"Enter the item you want to insert at position {i}:")
        row, col = (i - 1) // 3, (i - 1) % 3
        my_list[row][col] = item_insert

    print("\nUpdated crafting table:")
    display_crafting_table()
    check_crafting_table(inventory)
