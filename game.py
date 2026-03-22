import random
from player import Player
from game_world import GameWorld
from enemies import ENEMIES

class Game:
    def __init__(self):
        self.player = None
        self.world = GameWorld()
        self.current_location = None
        self.running = True
        self.in_combat = False
        self.current_enemy = None

    def start(self):
        print("\n" + "="*50)
        print("   WELCOME TO THE LOST FOREST")
        print("="*50)
        print("\nA mysterious adventure awaits you...")
        
        name = input("\nWhat is your name, adventurer? ").strip()
        self.player = Player(name)
        self.current_location = self.world.get_location("forest_entrance")
        
        print(f"\nWelcome, {name}!")
        self.show_location()
        self.main_loop()

    def show_location(self):
        print(self.current_location.display())

    def move(self, direction):
        if direction not in self.current_location.exits:
            print(f"You can't go {direction} from here.")
            return

        next_location = self.current_location.exits[direction]
        self.current_location = next_location
        print(f"\nYou travel {direction}...")
        self.show_location()

    def pick_up_item(self, item_name):
        if item_name not in self.current_location.items:
            print(f"There's no '{item_name}' here.")
            return

        self.current_location.items.remove(item_name)
        self.player.add_item(item_name)

    def use_item(self, item_name):
        if not self.player.has_item(item_name):
            print(f"You don't have a '{item_name}'.")
            return

        if item_name == "healing_potion":
            self.player.heal(50)
            self.player.remove_item(item_name)
            print("You drank the potion and felt much better!")
        else:
            print(f"You can't use '{item_name}' right now.")

    def encounter_enemy(self):
        enemies_list = list(ENEMIES.values())
        enemy = random.choice(enemies_list)
        self.current_enemy = enemy
        self.in_combat = True
        print(f"\n⚠️  A wild {enemy.name} appears!")
        print(f"{enemy.name} Health: {enemy.health}")

    def combat(self, action):
        if not self.in_combat or not self.current_enemy:
            return

        enemy = self.current_enemy

        if action == "attack":
            player_damage = random.randint(5, 15)
            enemy_damage = enemy.attack()

            enemy.take_damage(player_damage)
            self.player.take_damage(enemy_damage)

            print(f"\nYou attacked! Dealt {player_damage} damage.")
            print(f"{enemy.name} attacked you! You took {enemy_damage} damage.")
            print(f"\nYour health: {self.player.health}/{self.player.max_health}")
            print(f"{enemy.name} health: {enemy.health}/{enemy.max_health}")

            if not enemy.is_alive():
                self.win_combat()
            elif self.player.health <= 0:
                self.lose_combat()

        elif action == "defend":
            enemy_damage = max(1, enemy.attack() - 5)
            self.player.take_damage(enemy_damage)
            print(f"\nYou brace for impact! You took {enemy_damage} damage.")
            print(f"Your health: {self.player.health}/{self.player.max_health}")

        elif action == "flee":
            if random.random() > 0.5:
                print("\nYou managed to escape!")
                self.in_combat = False
                self.current_enemy = None
            else:
                enemy_damage = enemy.attack()
                self.player.take_damage(enemy_damage)
                print(f"\nYou couldn't escape! {enemy.name} hit you for {enemy_damage} damage.")
                print(f"Your health: {self.player.health}/{self.player.max_health}")

    def win_combat(self):
        exp = self.current_enemy.experience_reward
        self.player.gain_experience(exp)
        print(f"\n✓ Victory! You gained {exp} experience!")
        self.in_combat = False
        self.current_enemy = None

    def lose_combat(self):
        print(f"\n✗ You have been defeated by {self.current_enemy.name}...")
        self.running = False
        self.in_combat = False

    def main_loop(self):
        while self.running:
            try:
                if self.in_combat:
                    print("\n--- Combat ---")
                    action = input("What do you do? (attack/defend/flee): ").lower().strip()
                    if action in ["attack", "defend", "flee"]:
                        self.combat(action)
                    else:
                        print("Invalid action.")
                else:
                    print("\n--- Options ---")
                    command = input("What do you do? (move/take/use/status/explore/quit): ").lower().strip()

                    if command == "quit":
                        print("Thanks for playing!")
                        self.running = False

                    elif command == "move":
                        direction = input("Which direction? (north/south/east/west): ").lower().strip()
                        self.move(direction)
                        if random.random() < 0.3:  # 30% chance of enemy encounter
                            self.encounter_enemy()

                    elif command == "take":
                        item = input("What do you want to take? ").lower().strip()
                        self.pick_up_item(item)

                    elif command == "use":
                        item = input("What do you want to use? ").lower().strip()
                        self.use_item(item)

                    elif command == "status":
                        print(self.player.status())

                    elif command == "explore":
                        if random.random() < 0.4:
                            print("You found something interesting!")
                            self.encounter_enemy()
                        else:
                            print("You explore the area but find nothing.")

                    else:
                        print("Unknown command. Try: move, take, use, status, explore, or quit")

            except KeyboardInterrupt:
                print("\n\nGame interrupted. Thanks for playing!")
                self.running = False
            except Exception as e:
                print(f"An error occurred: {e}")

if __name__ == "__main__":
    game = Game()
    game.start()
