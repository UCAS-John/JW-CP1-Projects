class Player:
    def __init__(self, health, endurance, speed, mana, damage, crit_damage, crit_chance):
        self.health = health
        self.endurance = endurance
        self.speed = speed
        self.mana = mana
        self.damage = damage
        self.crit_damage = crit_damage
        self.crit_chance = crit_chance
        self.inventory = []
        self.dead_count = 0
        self.location = "Start"
        self.exp = 0
        self.upgrade_points = 0
        self.coins = 0

    def add_to_inventory(self, item):
        self.inventory.append(item)

    def use_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            print(f"Using {item}")  # Placeholder for item effect
        else:
            print("Item not found in inventory.")

    def upgrade(self, stat):
        if self.upgrade_points > 0:
            setattr(self, stat, getattr(self, stat) + self.upgrade_points)
            self.upgrade_points = 0
        else:
            print("No upgrade points available.")

    def earn_exp(self, points):
        self.exp += points
        while self.exp >= 100:
            self.exp -= 100
            self.upgrade_points += 5

    def upgrade_weapon(self, gemstone):
        print(f"Upgrading weapon with {gemstone}")  # Placeholder for gemstone effect


class Room:
    merchant_items = {
        "Broken dragon’s sword": 100,
        "Lost adventure’s armor": 400,
        "Healing potion": 30,
        "Mana potion": 30,
        "Love letter": 1000
    }

    def __init__(self, name, description, loot=None, monster=None, connections=None, puzzle=None, merchant=False, boss=False):
        self.name = name
        self.description = description
        self.loot = loot if loot else []
        self.monster = monster
        self.connections = connections if connections else {}
        self.puzzle = puzzle
        self.merchant = merchant
        self.boss = boss
        self.visited = False
        self.item_picked_up = False
        self.monster_defeated = False

    def explore(self, player):
        print(self.description)

        if self.monster and not self.monster_defeated:
            self.combat(player, self.monster)
            self.monster_defeated = True

        if self.loot and not self.item_picked_up:
            print(f"You found: {', '.join(self.loot)}")
            for item in self.loot:
                player.add_to_inventory(item)
            self.item_picked_up = True

        if self.puzzle:
            self.solve_puzzle(player)

        if self.merchant:
            self.interact_with_merchant(player)

        print(f"Available directions: {', '.join(self.connections.keys())}")
        direction = input("Choose a direction: ")
        if direction in self.connections:
            player.location = self.connections[direction]
        else:
            print("Invalid direction. Try again.")

    def combat(self, player, monster):
        print(f"Fighting {monster}")  # Placeholder monster logic
        while player.health > 0 and monster['health'] > 0:
            action = input("Choose an action (attack, defend, use item): ").lower()
            if action == "attack":
                monster['health'] -= player.damage
                print(f"You dealt {player.damage} damage.")
            elif action == "defend":
                print("You defended.")  # Placeholder for defense logic
            elif action == "use item":
                item = input("Enter item to use: ")
                player.use_item(item)

            if monster['health'] > 0:
                player.health -= monster['damage']
                print(f"The {monster['name']} dealt {monster['damage']} damage.")

        if player.health <= 0:
            player.dead_count += 1
            print(f"You were defeated by the {monster['name']}.")
        else:
            print(f"You defeated the {monster['name']}.")

    def solve_puzzle(self, player):
        print(self.puzzle)
        answer = input("Enter your answer: ")
        if answer.lower() == "correct":  # Placeholder for correct answer logic
            print("Puzzle solved! You earn some rewards and exp!")
            player.earn_exp(100)
        else:
            print("Incorrect answer. Sadly you can’t try it again.")

    def interact_with_merchant(self, player):
        print("Merchant offers the following items for sale:")
        for item, price in self.merchant_items.items():
            print(f"{item}: {price} coins")

        item_to_buy = input("Enter the name of the item to buy: ")
        if item_to_buy in self.merchant_items:
            price = self.merchant_items[item_to_buy]
            if player.coins >= price:
                player.coins -= price
                player.add_to_inventory(item_to_buy)
                print(f"You purchased {item_to_buy}.")
            else:
                print("Not enough coins.")
        else:
            print("Item unavailable.")


# Map Definition
Map = {
    "Start": Room(
        name="Raft",
        description="A small raft floating on the ocean, surrounded by mist.",
        loot=["Wooden Plank", "Strength Essence"],
        monster={"name": "Sea Serpent", "health": 50, "damage": 10},
        connections={"North": "Beach", "East": "Cavern"}
    ),
    # Add other rooms here...
}

# Game Loop
player = Player(health=100, endurance=50, speed=10, mana=50, damage=20, crit_damage=50, crit_chance=10)
current_room = "Start"

while player.dead_count < 3:
    room = Map[current_room]
    room.explore(player)
    current_room = player.location

    if player.health <= 0 or player.dead_count >= 3:
        print("Game Over")
        break
