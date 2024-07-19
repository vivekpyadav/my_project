class Entity:
    def __init__(self,name,health,chances,drops):
        self.name = name
        self.health = health
        self.chances = chances
        self.drops = drops

friendly_entity_data = [
    Entity('cow', 10, 2,('raw_beef','leather')),
    Entity('sheep', 10, 3,('raw_mutton','wool')),
    Entity('pig', 10, 4,('raw_porkchop',))
]

village_entity_data = [
    Entity('Villager', 20, 3,('stick',))
]

homo_entity_data = [
    Entity('iron_golem', 60, 0.3,('iron_ingot','flower'))
]

hostile_entity_data = [
    Entity('zombies', 20, 1,('rotten_flesh')),
    Entity('skeleton', 20, 0.7,('bone','arrow','bow')),
    Entity('creeper', 20, 0.5,('gunpowder',))

]
