class Inventory:
    def __init__(self):
        self.items = {}

    def pick_item(self, item, quantity=1):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity

    def throw_item(self, item, quantity=1):
        if item in self.items:
            if self.items[item] >= quantity:
                self.items[item] -= quantity
                if self.items[item] == 0:
                    del self.items[item]
                return True
            else:
                print(f"Not enough {item} in Inventory.")
                return False
        else:
            print(f"No {item} in Inventory")

    def eat_item(self, item):
        food_items = ['apple', 'carrot', 'potato', 'bread']
        if item in self.items:
            if item in food_items:
                self.items[item] -= 1
                if self.items[item] == 0:
                    del self.items[item]
            else:
                print(f"{item} is not a valid food item.")
            return True
        else:
            print(f"No {item} in Inventory")

    def shift_item(self, item, new_position):
        if item in self.items:
            self.items = {new_position: self.items.pop(item)}
        else:
            print(f"No {item} in Inventory.")

    def select_item(self, item):
        if item in self.items:
            return item
        else:
            print(f"No {item} in Inventory.")
            return None

    def display_inventory(self):
        slots = []
        dash_lines = []

        for item, quantity in self.items.items():
            slot = f"|{item} = {quantity}|"
            dash_line = "+" + ("-" * (len(slot) - 2)) + "+"

            slots.append(slot)
            dash_lines.append(dash_line)

        print(" - ".join(dash_lines))
        print(" - ".join(slots))
        print(" - ".join(dash_lines))

    def has_items(self, required_items):
        for item, quantity in required_items.items():
            if self.items.get(item, 0) < quantity:
                return False
        return True

    def use_items(self, required_items):
        if self.has_items(required_items):
            for item, quantity in required_items.items():
                self.throw_item(item, quantity)
            return True
        return False

