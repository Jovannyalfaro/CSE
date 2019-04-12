class Item(object):
    def __init__(self, name):
        self.name = name



class Weapon(Item):
    def __init__(self, name, damage):
        super(Weapon, self).__init__(name)
        self.damage = damage

class sword(Weapon)



class Armor(Item):
    def __init__(self, name, armor_amt):
        super(Armor, self).__init__(name)
        self.name = name
        self.armor_amt = armor_amt


class Character(object):
    def __init__(self, name, health: int, weapon, armor, damage):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor
        self.damage = damage

    def take_damage(self, damage:int):
        if self.armor.armor_amt > damage:
            print("no damage is done because of some godly armor")
        else:
            self.health -= (damage - self.armor.armor_amt)
        print("%s has %d health left" % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s for %d damage" % (self.name, target.name, self.weapon.damage))




# Items



# Characters
monster = Character("monster", 100, )
knight = Character("knight", 100, sword,)
horse = Character("horse", 100)

monster.attack(knight)
monster2.attack(knight)
monster3.attack(knight)
monster4.attack(knight)

