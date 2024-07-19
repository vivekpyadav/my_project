class Block:
    def __init__(self,name,mining_speed,priority,rarity,found_at):
        self.name = name
        self.mining_speed = mining_speed
        self.priority = priority
        self.rarity = rarity
        self.found_at = found_at

blocks_data = [
    Block('netherack', 0.5, 73, 'common','all'),
    Block('gold_nugget_ore', 2, 8, 'common','all'),
    Block('quartz_ore', 2, 10, 'common','all'),
    Block('gravel', 1, 4, 'common','middlebelow'),
    Block('soul_sand', 1, 3, 'common','below'),
    Block('blackstone', 1, 20, 'common','middlebelow'),
    Block('netherite', 10, 0.4, 'precious','below')
]
