class Block:
    def __init__(self, name, mining_speed, priority, rarity, found_at):
        self.name = name
        self.mining_speed = mining_speed
        self.priority = priority
        self.rarity = rarity  # 'common', 'rare', 'precious'
        self.found_at = found_at # all , above , above_middle , middle , middle_below , below

blocks_data = [
    Block('stone', 1, 60, 'common','above'),
    Block('tuff', 1, 12, 'common','middle_below'),
    Block('deepslate', 2, 47, 'common','middle_below'),
    Block('gravel', 2, 9,'common','all'),
    Block('iron_ore', 3, 10, 'common','all'),
    Block('coal', 3, 16, 'common','above_middle'),
    Block('copper', 3, 14, 'common','above'),
    Block('lapis', 4, 11, 'rare','middle_below'),
    Block('redstone', 5, 4, 'rare','middle_below'),
    Block('gold_ore', 7, 5, 'rare','middle_below'),
    Block('obsidian', 20, 7, 'rare','middle_below'),
    Block('emerald_ore', 9, 1, 'precious','below'),
    Block('diamond_ore', 10, 2, 'precious','below')
]

