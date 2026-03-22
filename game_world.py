class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.npcs = []
        self.items = []
        self.visited = False

    def add_exit(self, direction, location):
        self.exits[direction] = location

    def add_item(self, item):
        self.items.append(item)

    def add_npc(self, npc):
        self.npcs.append(npc)

    def display(self):
        text = f"\n{'='*50}\n{self.name}\n{'='*50}\n{self.description}\n"
        
        if self.items:
            text += f"\nItems here: {', '.join(self.items)}\n"
        
        if self.npcs:
            text += f"People: {', '.join([npc.name for npc in self.npcs])}\n"
        
        if self.exits:
            text += f"\nExits: {', '.join(self.exits.keys())}\n"
        
        return text

class GameWorld:
    def __init__(self):
        self.locations = {}
        self._setup_world()

    def _setup_world(self):
        # Create locations
        forest_entrance = Location(
            "Forest Entrance",
            "You stand at the edge of a dense forest. Tall trees surround you, and the sound\nof birds echoes through the air. The path ahead is dark and mysterious."
        )
        
        deep_forest = Location(
            "Deep Forest",
            "The trees are thicker here. You notice strange markings on some trunks.\nThe air feels cold and eerie."
        )
        
        old_cabin = Location(
            "Old Cabin",
            "A weathered wooden cabin stands before you. The door creaks in the wind.\nSmoke wisps from the chimney - someone might be home."
        )
        
        mountain_path = Location(
            "Mountain Path",
            "You've reached a narrow path up the mountain. The view below is breathtaking.\nYou can see the entire forest from here."
        )
        
        # Connect locations
        forest_entrance.add_exit("north", deep_forest)
        forest_entrance.add_exit("east", mountain_path)
        
        deep_forest.add_exit("south", forest_entrance)
        deep_forest.add_exit("west", old_cabin)
        
        old_cabin.add_exit("east", deep_forest)
        
        mountain_path.add_exit("west", forest_entrance)
        
        # Add items
        forest_entrance.add_item("rusty_key")
        deep_forest.add_item("healing_potion")
        mountain_path.add_item("ancient_map")
        
        # Store locations
        self.locations = {
            "forest_entrance": forest_entrance,
            "deep_forest": deep_forest,
            "old_cabin": old_cabin,
            "mountain_path": mountain_path
        }

    def get_location(self, location_id):
        return self.locations.get(location_id)
