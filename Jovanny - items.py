class Item(object):
    def __init__(self, name):
        self.name = name



class Weapon(Item):
    def __init__(self, damage, name):
        super(Weapon, self).__init__(name)
        self.damage = damage


class Character(Item):
    def __init__(self, health, name):
         self.health = health












directions = ['north', 'south', 'east', 'west', 'up', 'down']
short_directions = ['n', 's', 'e', 'w', 'u', 'd']

if command.lower() in short_directions:
    pos = short_directions.index(command.lower())
    command = directions[pods]

















