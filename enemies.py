import random

class Enemy:
    def __init__(self, name, health, attack_damage, experience_reward):
        self.name = name
        self.health = health
        self.max_health = health
        self.attack_damage = attack_damage
        self.experience_reward = experience_reward

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def attack(self):
        # Add randomness to attacks
        variance = random.randint(-5, 5)
        return max(1, self.attack_damage + variance)

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"{self.name} (Health: {self.health}/{self.max_health})"

# Enemy types
ENEMIES = {
    "wolf": Enemy("Wolf", 30, 8, 50),
    "goblin": Enemy("Goblin", 20, 5, 30),
    "dark_knight": Enemy("Dark Knight", 60, 15, 150),
    "forest_guardian": Enemy("Forest Guardian", 50, 12, 100)
  }
