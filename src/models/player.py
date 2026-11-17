class Player:
    def __init__(self, name):
        self.name = name
        
        self.inventory = {}
        
        self.maxHp = 10
        self.currentHP = 10
        
        self.lvl = 1
        self.xp = 0

    def addToInventory(self, item, itemQuantity):
        
        if item in self.inventory: 
            self.inventory[item] += itemQuantity

        else: 
            self.inventory[item] = itemQuantity
        
        print(self.inventory)
        
        