class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.max_health = 100
        self.inventory = []
        self.location = "forest_entrance"
        self.experience = 0

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def heal(self, amount):
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health

    def add_item(self, item):
        self.inventory.append(item)
        print(f"✓ Added {item} to inventory")

    def remove_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return True
        return False

    def has_item(self, item):
        return item in self.inventory

    def gain_experience(self, amount):
        self.experience += amount

    def status(self):
        return f"\n=== {self.name} ===\nHealth: {self.health}/{self.max_health}\nExperience: {self.experience}\nInventory: {', '.join(self.inventory) if self.inventory else 'Empty'}"
        
