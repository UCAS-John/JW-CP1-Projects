import random
import time

class Player:
    def __init__(self, name, health, endurance, speed, mana, damage, crit_damage, crit_chance, coins, weapon, armor):
        self.name = name
        self.health = health
        self.endurance = endurance
        self.speed = speed
        self.mana = mana
        self.damage = damage
        self.crit_damage = crit_damage
        self.crit_chance = crit_chance
        self.coins = coins
        self.weapon = weapon
        self.armor = armor
        self.inventory = {
            "Healing Potion": 0,
            "Mana Potion": 0
        }
        self.dead_count = 0
        self.location = "Start"
        self.exp = 0
        self.upgrade_points = 0
        self.coins = 0
        self.skills = {
            "Slash": {"mana": 0, "damage": 50},
            "Fire": {"mana": 35, "damage": 100},
            "Stunt": {"mana": 30, "damage": 40},
            "Heal": {"mana": 0, "damage": 30},
        }
    
    def rest(self):
        self.health += (self.health*0.15)
        self.mana += (self.health*0.15)

    def attack(self, skill):
        if random.random() < (self.crit_chance / 100):
            return self.damage * (1 + (self.crit_damage / 100)) * skill["damage"]
        else:
            return self.damage * skill["damage"]
        
    def take_damage(self, monster_name):
        diff = self.speed = monsters[monster_name].speed
        if diff > 0:
            if random.random() < (diff / 100):
                print(f"{self.name} dodge the attack!")
        else:
            damage_take = monsters[monster_name].damage - (self.endurance*2)
            self.health -= damage_take
            print(f"{self.name} take {damage_take}!")

    def add_to_inventory(self, types, item):
        if types == "coins":
            self.coins += item
            return
        elif types == "exp":
            self.earn_exp(item)
            return
        elif types == "essence":
            if item == "damage":
                self.damage *= 1.2
            elif item == "crit chance":
                self.crit_chance += 20
            elif item == "crit damage":
                self.crit_damage += 100
            elif item == "health":
                self.health *= 1.2
            else:
                self.speed += 10
        elif types == "Healing Potion" or types == "Mana Potion":
            self.inventory[types] += item
        else:
            self.inventory.append(item)
            return

    def upgrade(self, stat):
        setattr(self, stat, getattr(self, stat) + self.upgrade_points)
        self.upgrade_points = 0

    def earn_exp(self, points):
        self.exp += points
        if self.exp >= 100:
            self.upgrade_points += (int(self.exp/100)) * 5
            self.exp = self.exp % 100

    def use_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            if item == "Healing Potion":
                self.health += 30
            elif item == "Mana Potion":
                self.mana += 20
            print(f"Used {item}")

class weapon:
    def __init__(self, damage, crit_chance, crit_damage, mana):
        self.damage = damage
        self.crit_chance = crit_chance
        self.crit_damage = crit_damage
        self.mana = mana
    
    def upgrade(self, gemstone):
        if gemstone == "Ruby":
            self.crit_damage += 40
        elif gemstone == "Sapphire":
            self.mana += 50
        elif gemstone == "Jade":
            self.crit_chance += 10
        print(f"Upgraded weapon with {gemstone}")
class armor:
    def __init__(self, health, endurance, speed):
        self.health = health
        self.endurance = endurance
        self.speed = speed

    def upgrade(self, gemstone):
        if gemstone == "Ruby":
            self.endurance += 40
        elif gemstone == "Sapphire":
            self.speed += 50
        elif gemstone == "Jade":
            self.health += 10
        print(f"Upgraded weapon with {gemstone}")
class Monster:
    def __init__(self, name, health, damage, speed):
        self.name = name
        self.health = health
        self.damage = damage
        self.speed = speed

class Room:
    def __init__(self, name, description, loot, monster, connections, requirement=None, puzzle=None, merchant=False, boss=False):
        self.name = name
        self.description = description
        self.loot = loot
        self.monster = monster
        self.connections = connections
        self.requirement = requirement
        self.puzzle = puzzle
        self.merchant = merchant
        self.boss = boss
        self.visited = False
        self.item_picked_up = False
        self.monster_defeated = False
        self.merchant_item = {
            "Broken Dragon's sword": 100,
            "Lost adventure's armor": 400,
            "Healing Potion": 30,
            "Mana potion": 30,
            "Love leterr???": 1000
        }


    def explore(self, player):
        print(self.description)
        if self.monster and not self.monster_defeated:
            self.combat(player)
            self.monster_defeated = True
        
        if self.monster != None:
            self.combat(player)

        if self.puzzle:
            self.solve_puzzle(player)

        if self.merchant:
            self.interact_with_merchant(player)
        
        print(f"Available directions: {', '.join(self.connections)}")
        direction = input("Which direction do you want to go? ")
        if direction in self.connections:
            player.location = direction
        else:
            print("Invalid direction. Try again.")

    def combat(self, player):
        print(f"Fighting {self.monster.name}")
        while player.health > 0 and self.monster.health > 0:
            action = input("Choose attack or potion: ")
            if action == "attack":
                print(player.skills)
                self.monster.health -= player.attack(player.skills)
            elif action == "potion":
                print(f"Potions in inventory: {player.inventory}")
                item = input("Which potion do you want to use? ")
                player.use_item(item)

            if self.monster.health > 0:
                player.take_damage(self.monster)

        if player.health <= 0:
            player.dead_count += 1
            print(f"You were defeated by the {self.monster.name}")
        else:
            print(f"You defeated the {self.monster.name}")
            self.monster_defeated = True
        
        if self.loot and not self.item_picked_up:
            print("You get rewards for killing monster:")
            for item, types in self.loot.items():
                print(f"{types}: {item}")
                player.add_to_inventory(types, item)
            self.item_picked_up = True

    def solve_puzzle(self, player):
        print(self.puzzle)
        answer = input("Your answer: ")
        if answer == "correct_answer":
            print("Puzzle solved! You earn some rewards and exp!")
            player.earn_exp(100)
        else:
            print("Incorrect answer. Sadly you can't try it again.")

    def interact_with_merchant(self, player):
        print("Merchant offers the following items for sale:")

        for item, price in self.merchant_item:
            print(f"{item}: {price} coins")

        item_to_buy = input("Which item would you like to buy? ")

        if item_to_buy in self.merchant_item:
            player.coins -= self.merchant_item[item_to_buy]
            player.add_to_inventory(item_to_buy)
            print(f"Item {item_to_buy} purchased.")
        else:
            print("Item unavailable.")

        user_choice = input("Do you want to interact again? (1 for yes, any key for no): ")
        if user_choice == "1":
            self.interact_with_merchant(player)


# Define monsters
monsters = {
    "Sea Serpent": Monster("Sea Serpent", 120, 15),
    "Crab King": Monster("Crab King", 180, 20),
    "Jungle Tiger": Monster("Jungle Tiger", 150, 25),
    "Golem Guardian": Monster("Golem Guardian", 300, 30),
    "Ice Dragon": Monster("Ice Dragon", 400, 45),
    "Cave Bat": Monster("Cave Bat", 80, 10),
    "Fire Drake": Monster("Fire Drake", 250, 40),
    "Dragon King": Monster("Dragon King", 1000, 50),
}

armors = {
    "Leather Armor": armor(50, 10, 5),
    "Jungle Armor": armor(100, 20, 15),
    "Lost Adventure's Armor": armor(250, 50, 30)
}

weapons = {
    "Wooden Sword": weapon(10, 3, 10),
    "Shell Sword": weapon(20, 10, 30),

}

rooms = {
    "Start": Room(
        name="Raft",
        description="A small raft floating on the ocean, surrounded by mist.",
        loot={"Wooden Sword": "weapons", 
            "Leahter Armor": "armor",
            "essence": "damage", 
            "coins": 50,
            "exp": 50},
        monster="Sea Serpent",
        connections={"North": "Beach", "East": "Lava Pit"}
    ),
    "Beach": Room(
        name="Beach",
        description="A peaceful beach with golden sand, waves crashing gently.",
        loot={"Shell Sword": "sword", 
            "Healing Potion": 1,
            "essence": "crit chance", 
            "coins": 60,
            "exp": 100},
        monster="Crab King",
        connections={"South": "Start", "North": "Cavern", "West": "Merchant's Hut"}
    ),
    "Jungle": Room(
        name="Jungle",
        description="A dense jungle with tall trees, birds chirping in the distance, and mysterious rustling sounds.",
        loot={"Jungle Armor": "armor", 
            "Mana Potion": 1,
            "essence": "health", 
            "coins": 80,
            "exp": 100},
        monster="Jungle Tiger",
        puzzle="Solve a riddle to progress.",
        connections={"South": "Lava Pit", "North": "Temple"}
    ),
    "Merchant's Hut": Room(
        name="Merchant's Hut",
        description="A small, cozy hut where a merchant sells various items.",
        loot={"gemstone": "Sapphire", 
            "exp": 150},
        monster=None,
        merchant=True,
        connections={"East": "Beach"}
    ),
    "Temple": Room(
        name="Temple",
        description="An ancient stone temple covered in vines, emitting a faint glow.",
        loot={"gemstone": "Ruby", 
            "key": "Secret Key",
            "exp": 200},
        monster="Golem Guardian",
        connections={"South": "Jungle", "North": "Mountain", "West": "Cavern"}
    ),
    "Mountain": Room(
        name="Mountain",
        description="A steep mountain peak with icy winds howling around you.",
        loot={"gemstone": "Jade", 
            "skill": "iron shield",
            "exp": 400},
        monster="Ice Dragon",
        connections={"South": "Temple", "West": "Hidden Cave", "North": "Lair"}
    ),
    "Hidden Cave": Room(
        name="Hidden Cave",
        description="A dark cave with echoes of mysterious sounds and sparkling crystals.",
        loot={"essence": "crit damage", 
            "coins": "1000",
            "exp": 300},
        monster=None,
        puzzle="Solve the crystal alignment puzzle to access treasure.",
        requirement="Secret Key",
        connections={"East": "Mountain", "South": "Cavern"}
    ),
    "Cavern": Room(
        name="Cavern",
        description="A damp, dark cavern with strange echoes.",
        loot={"essence": "speed", 
            "coins": 200,
            "exp": 200},
        monster="Cave Bat",
        connections={"West": "Start", "East": "Lava Pit"}
    ),
    "Lava Pit": Room(
        name="Lava Pit",
        description="A dangerous pit of bubbling lava, with scorching heat.",
        loot={ "coins": 200,
            "exp": 500},
        monster="Fire Drake",
        puzzle="Find the safe path across the lava.",
        connections={"North": "Jungle", "West": "Start"}
    ),
    "Dragon's Lair": Room(
        name="Dragon's Lair",
        description="A vast cavern with treasure hoards and dragon bones scattered around.",
        loot="Victory",
        monster="Dragon King",
        connections={"South": "Mountain"}
    ),
}

def main():
    print("Welcome to the game!")
    username = input("Enter your name: ")
    player = Player(username, 100, 10, 50, 10, 50, 10)

    current_room = "Start"
    timer = 0  # Track the time in seconds

    while player.dead_count < 3 and timer <= 1800:
        action = input("What will you do? (explore/rest/upgrade): ").lower()
        if action == "explore":
            rooms[current_room].explore(player)
        elif action == "rest":
            print("You are resting this action take 10 seconds!")
            print("You rest and gain back 15% of hp and mana")
            player.rest()
        elif action == "upgrade":
            stat = input("Which stat would you like to upgrade? (health/speed/mana/damage): ").lower()
            player.upgrade(stat)

        if player.health <= 0 or player.dead_count >= 3:
            print("Game Over")
            break

if __name__ == "__main__":
    main()
