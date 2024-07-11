from inventory import Inventory
from crafting_table import display_crafting_table, craft

inventory = Inventory()

print("Welcome to Minecraft!")

if __name__ == "__main__":
    while True:
        print("""
    Pick item(1)
    Select item(2)
    Throw item(3)
    Shift item(4)
    Craft item(5)
    Eat food item(6)
    Exit(7)
    """)
        inventory.display_inventory()
        choice = input("What do you want to do? ")
        if choice == '1':
            inventory.pick_item(input("What do you want to pick? "), int(input("How many? ")))
            print("Added")
        elif choice == '2':
            inventory.select_item(input("What do you want to select? "))
            print("Selected")
        elif choice == '3':
            inventory.throw_item(input("What item to throw? "), int(input("How many? ")))
            print("Thrown")
        elif choice == '4':
            inventory.shift_item(input("Enter the item: "), int(input("Enter the new position: ")))
            print("Shifted")
        elif choice == '5':
            display_crafting_table()
            craft()
        elif choice == '6':
            inventory.eat_item(input("What do you want to eat? "))
            print("Eaten")
        elif choice == '7':
            break
        else:
            print("Invalid choice")

