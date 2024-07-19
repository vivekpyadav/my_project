import os
import json

class Item:
    def __init__(self, name):
        self.name = name  # stores item name

class Inventory:
    def __init__(self):
        self.items = {}  # Dictionary to store items and their quantities

    def add_item(self, item, quantity):
        # Initialize the item's stacks if not present
        if item.name not in self.items:
            self.items[item.name] = []

        # Fill existing stacks first
        for stack in self.items[item.name]:
            if stack['quantity'] < 64:  # if stack is not full
                available_space = 64 - stack['quantity']  # calculate the space left in stack
                add_amount = min(available_space, quantity)  # add much as possible up to available_space
                stack['quantity'] += add_amount
                quantity -= add_amount  # update remaining quantity to add
                if quantity == 0:
                    break

        # Add new stacks if needed
        while quantity > 0:
            add_amount = min(64, quantity)  # add up to 64 items per stack
            self.items[item.name].append({'item': item, 'quantity': add_amount})  # Add new stack
            quantity -= add_amount  # update remaining quantity to add

    def remove_item(self, item_name, quantity=1):
        if item_name in self.items:  # check if item exists or not
            while quantity > 0 and self.items[item_name]:  # Remove specified quantity from inventory
                stack = self.items[item_name][0]  # Get the first stack of item
                if stack['quantity'] > quantity:
                    stack['quantity'] -= quantity  # reduce quantity in stack
                    quantity = 0  # requested items removed
                else:
                    quantity -= stack['quantity']  # reduce quantity to remove remaining items
                    self.items[item_name].pop(0)  # remove stack from inventory

            if not self.items[item_name]:  # remove item entry
                del self.items[item_name]

            if quantity > 0:
                print("Not enough items to remove.")
        else:
            print("Item not found in Inventory!")

    def show_inventory(self):
        count = 0
        for item_name, stacks in self.items.items():
            for stack in stacks:
                slot = f"[{item_name} = {stack['quantity']}]"
                print(slot.ljust(18), end=" ")
                count += 1
                if count % 3 == 0:
                    print()
        print("\n")

    def load_inventory(self, data):
        self.items = {}
        for item_name, stacks in data.items():
            self.items[item_name] = [{'item': Item(item_name), 'quantity': stack['quantity']} for stack in stacks]

    def save_inventory(self):
        return {item_name: [{'quantity': stack['quantity']} for stack in stacks] for item_name, stacks in self.items.items()}

