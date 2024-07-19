class FoodItems:

    def __init__(self,name,catagory,fillhunger):
        self.name = name
        self.catagory = catagory
        self.fillhunger = fillhunger

food_items_data = [
    FoodItems('carrot', 'raw', 1.5),
    FoodItems('potato', 'raw', .5),
    FoodItems('apple', 'raw', 2),
    FoodItems('baked_potato', 'cooked', 2.5),
    FoodItems('cooked_mutton', 'cooked', 3),
    FoodItems('cooked_chicken', 'cooked', 3),
    FoodItems('cooked_steak', 'cooked', 4),
    FoodItems('cooked_porkchop', 'cooked', 4)
]
