import random
import time

def line():
    print("---------------------------------------------------------------------------")
class Player:
    def __init__(self, name, health, endurance, speed, mana, damage, crit_damage, crit_chance, coins):
        self.name = name
        self.max_health = health
        self.health = health
        self.endurance = endurance
        self.speed = speed
        self.max_mana = mana
        self.mana = mana
        self.damage = damage
        self.crit_damage = crit_damage
        self.crit_chance = crit_chance
        self.coins = coins
        self.weapon = None
        self.armor = None
        self.inventory = {
            "healing potion": 0,
            "mana potion": 0
        }
        self.dead_count = 0
        self.location = "Start"
        self.previous_location = "Start"
        self.level = 0
        self.exp = 0
        self.upgrade_points = 0
        self.coins = 0
        self.skills = {
            "slash": {"mana": 0, "damage": 20},
            "fire": {"mana": 35, "damage": 50},
            "stunt": {"mana": 30, "damage": 10},
            "heal": {"mana": 0, "damage": 30}
        }

    def open_inventory(self):
        line()
        print(f"Armor: {self.armor}")
        print(f"Weapons: {self.weapon}")
        print(f"coins: {self.coins}")
        for item, amount in self.inventory.items():
            print(f"{item}: {amount}")

    def change_armor(self, armor):
        if not self.armor == None:
            self.max_health -= armors[self.armor].health
        self.max_health += armors[armor].health
        
    def rest(self):
        line()
        self.heal(self.max_health*0.15)
        self.mana_regen(self.max_mana*0.15)
        time.sleep(10)
    
    def mana_regen(self, mana):
        if self.mana + mana > self.max_mana:
            self.mana = self.max_health
        else:
            self.mana += mana
        print(f"You regen {mana} mana")

    def heal(self, hp):
        if self.health + hp > self.max_health:
            self.health = self.max_health
        else:
            self.health += hp

        print(f"You heal {hp} hp!")

    def attack(self, skill):

        skill = skill.lower()

        if skill == "heal":
            self.heal(self.skills[skill]["damage"])
            return 0

        if self.weapon != None:
            weapon = weapons[self.weapon]
            damage = self.damage+weapon.damage
            crit_chance = self.crit_chance+weapon.crit_chance
            crit_damage = self.crit_damage+weapon.crit_damage
        else:
            damage = self.damage
            crit_damage = self.crit_damage
            crit_chance = self.crit_chance

        self.mana -= self.skills[skill]["mana"]

        if random.random() < (crit_chance / 100):
            damage_dealt = ((damage) + self.skills[skill]["damage"]) * (1 + (crit_damage / 100)) 
            print(f"Critical Damage {damage_dealt}!")
            return damage_dealt

        damage_dealt = damage + self.skills[skill]["damage"]
        print(f"You deal {damage_dealt} damage")
        return damage_dealt
        
    def take_damage(self, monster_name):
        if self.armor != None:
            armor = armors[self.armor]
            endurance = self.endurance+armor.endurance
            speed = self.speed+armor.speed
        else:
            endurance = self.endurance
            speed = self.speed

        diff = speed - monsters[monster_name].speed

        if diff > 0:
            if random.random() < (diff / 100):
                print(f"{self.name} dodge the attack!")

        damage_take = monsters[monster_name].damage - (endurance*2)
        if not damage_take < 0:
            self.health -= damage_take
            print(f"{self.name} take {damage_take} damage!")
        else:
            print("You Tank the damage!")

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
        elif types == "armor":
            self.change_armor(item)
            self.armor = item
        elif types == "weapon":
            self.weapon = item
            self.max_mana += weapons[item].mana

    def stats_view(self):
        line()
        print("This is your current stats")
        print(f"Level: {self.level}")
        print(f"exp: {self.exp}/100")
        print(f"Health: {self.max_health}")
        print(f"Endurance: {self.endurance}")
        print(f"Mana: {self.max_mana}")
        print(f"Damage: {self.damage}")
        print(f"Critical Chance: {self.crit_chance}")
        print(f"Critical Damage: {self.crit_damage}")
        print(f"Current upgrade points: {self.upgrade_points}")

    def upgrade(self):

        line()
        print("This is your current stats")
        print(f"1. Health: {self.max_health}")
        print(f"2. Mana: {self.max_mana}")
        print(f"3. Damage: {self.damage}")
        print(f"4. Critical Chance: {self.crit_chance}")
        print(f"5. Critical Damage: {self.crit_damage}")
        print(f"Current upgrade points: {self.upgrade_points}")

        try:
            stat = int(input("Enter number of stats to upgrade: "))
            upgrade_point = int(input("Enter amount of upgrade points to use: "))
        except ValueError:
            print("Please enter an integers!")
            return
        if stat not in range(1, 6):
            print("Please Enter number beetween 1-5") 
            return
        elif upgrade_point > self.upgrade_points or upgrade_point < 0:
            print("Please Enter valid amount of upgrade points")
            return

        match stat:
            case 1:
                upgrade = 10*upgrade_point
                print(f"Your max health increase by {upgrade}")
                self.max_health += upgrade
            case 2:
                upgrade = 10*upgrade_point
                print(f"Your max mana increase by {upgrade}")
                self.max_mana += upgrade
            case 3:
                upgrade = 5*upgrade_point
                print(f"Your damage increase by {upgrade}")
                self.damage += upgrade
            case 4:
                upgrade = 2*upgrade_point
                print(f"Your critical chance increase by {upgrade}")
                self.crit_chance += upgrade
            case 5:
                upgrade = 11*upgrade_point
                print(f"Your critical damage increase by {upgrade}")
                self.crit_damage += upgrade


    def earn_exp(self, points):
        self.exp += points
        if self.exp >= 100:
            self.upgrade_points += (int(self.exp/100)) * 5
            self.level += int(self.exp/100)
            self.exp = self.exp % 100

    def use_item(self, item):
        if item in self.inventory and self.inventory[item] > 0:
            self.inventory.remove(item)
            if item == "Healing Potion":
                self.health += 30
            elif item == "Mana Potion":
                self.mana += 20
            print(f"Used {item}")
        else:
            print("Item unavailabe")

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
        self.puzzle_fail = False
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
        line()
        print(f"You are in the {self.name}")
        print(self.description)
        self.visited = True
        
        if self.monster != None and not self.monster_defeated:
            self.combat(player)

        if self.puzzle:
            self.solve_puzzle(player)

        if self.merchant:
            self.interact_with_merchant(player)
        
        print(f"Available directions:")
        for connect in self.connections.keys():
            if rooms[self.connections[connect]].visited == True:
                print(f"{connect}: {self.connections[connect]}")
            else:
                print(f"{connect}: Unknown")
        direction = input("Which direction do you want to go? ").lower()
        if direction in self.connections:
            player.previous_location = player.location
            player.location = self.connections[direction]
            line()
            print(f"You enter the {player.location}")
        else:
            line()
            print("Invalid direction. Try again.")

    def combat(self, player):
        line()
        print(f"Fighting {self.monster}")
        monster = monsters[self.monster]

        while player.health > 0 and monster.health > 0:

            line()
            print(f"{self.monster} | {monster.health} HP")
            print(f"{player.name} | HP {player.health} | MANA {player.mana}")

            while True:
                action = input("Choose (attack/potion/escape): ").lower()

                if action not in ['attack','potion','escape']:
                    print("Invalid Action")
                    continue
                break

            if action == "attack":
                while True:
                    line()
                    for skill in player.skills.keys(): 
                        print(f"{skill} | Mana {player.skills[skill]["mana"]} | Damage {player.skills[skill]["damage"]}")   
                    choose_skill = input("Enter your skill: ").lower()
                    line()
                    if choose_skill not in player.skills.keys():
                        print("invalid skill")
                        continue
                    if player.mana - player.skills[skill]["mana"] < 0:
                        print("Not enough mana\n Choose skill again!!!")
                        continue
                    else:
                        monsters[self.monster].health -= player.attack(choose_skill)
                        break
            elif action == "potion":
                line()
                print("Potions in inventory:")
                for potion, amount in player.inventory.items():
                    print(f"{potion}: {amount}")
                item = input("Which potion do you want to use? ").lower()
                player.use_item(item)
            elif action == "escape":
                line()
                print(f"You back in to the {player.previous_location}")
                player.location = player.previous_location
                return

            if monsters[self.monster].health > 0:
                player.take_damage(self.monster)

        if player.health <= 0:
            player.dead_count += 1
            line()
            print(f"You were defeated by the {self.monster}")
            line()
        else:
            line()
            print(f"You defeated the {self.monster}")
            line()
            self.monster_defeated = True
        
        if self.loot and not self.item_picked_up:
            line()
            print("You get rewards for killing monster:")
            for item, types in self.loot.items():
                print(f"{item}: {types}")
                player.add_to_inventory(types, item)
            self.item_picked_up = True
            line()

    def solve_puzzle(self, player):
        # Lava Pit Puzzle
        def solve_lava_pit():
            sequence = ["Fire", "Light", "Light"]
            user_sequence = []
            print("Clue:")
            print("\"One step for fire, two steps for light,\nAvoid the darkness, stay in sight.\nRepeat the pattern till the end,\nTo reach the treasure, my friend.\"")

            while len(user_sequence) < len(sequence):
                choice = input("Choose your next platform (Fire, Light, Darkness): ").capitalize()
                user_sequence.append(choice)

                if user_sequence != sequence[:len(user_sequence)]:
                    print("The platform shakes! You've chosen incorrectly. Resetting...")
                    return False

            print("You crossed the lava pit successfully!")
            return True

        lava_pit_puzzle = Puzzle("Lava Pit", "One step for fire, two steps for light...", solve_lava_pit)

        # Jungle Puzzle
        def solve_jungle_puzzle():
            correct_sequence = ["C", "E", "G", "D", "A"]
            user_sequence = []

            print("Clue:")
            print("\"Nature’s melody unlocks the way,\nFollow the rhythm the jungle plays.\"")
            print("Listen carefully to the bird calls and reproduce the melody.")

            while len(user_sequence) < len(correct_sequence):
                note = input("Enter the next note (C, D, E, G, A): ").capitalize()
                user_sequence.append(note)

                if user_sequence != correct_sequence[:len(user_sequence)]:
                    print("The vines tighten! You've chosen incorrectly. Resetting...")
                    return False

            print("The vines part, revealing a hidden path!")
            return True

        jungle_puzzle = Puzzle("Jungle", "Nature’s melody unlocks the way...", solve_jungle_puzzle)

        # Hidden Cave Puzzle
        def solve_hidden_cave():
            print("Clue:")
            print("\"Reflect the truth, dispel the lies,\nAlign the crystals where light complies.\nThe key lies where red and blue collide.\"")

            crystals = {"Red": False, "Blue": False, "Green": False, "Yellow": False}

            print("You see crystals: Red, Blue, Green, Yellow. Choose two to place.")

            first = input("Choose the first crystal to place: ").capitalize()
            second = input("Choose the second crystal to place: ").capitalize()

            if first == "Red" and second == "Blue" or first == "Blue" and second == "Red":
                print("The beams of light converge into a purple glow. The pedestal activates!")
                return True
            else:
                print("The crystals fail to align. Try again.")
                return False

        hidden_cave_puzzle = Puzzle("Hidden Cave", "Reflect the truth, dispel the lies...", solve_hidden_cave)


if __name__ == "__main__":
    main()


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

    def __init__(self, name, health, endurance, damage, speed):
        self.name = name
        self.health = health
        self.endurance = endurance
        self.damage = damage
        self.speed = speed

    def take_damage(self, player, damage):

        endurance = self.endurance
        speed = self.speed

        diff = speed - player.speed

        if diff > 0:
            if random.random() < (diff / 100):
                print(f"{self.name} dodge the attack!")

        damage_take = damage - (endurance*2)
        self.health -= damage_take
        print(f"{self.name} take {damage_take}!")

# Define monsters
monsters = {
    "Sea Serpent": Monster("Sea Serpent", 120, 5, 25, 10),
    "Crab King": Monster("Crab King", 180, 10, 20, 25),
    "Jungle Tiger": Monster("Jungle Tiger", 150, 15, 40, 30),
    "Golem Guardian": Monster("Golem Guardian", 300, 20, 20, 5),
    "Ice Dragon": Monster("Ice Dragon", 400, 40, 40, 30),
    "Cave Bat": Monster("Cave Bat", 80, 10, 30, 50),
    "Fire Drake": Monster("Fire Drake", 250, 40, 50, 30),
    "Dragon King": Monster("Dragon King", 1000, 50, 80, 60),
}

armors = {
    "Leather Armor": armor(50, 10, 5),
    "Jungle Armor": armor(100, 20, 15),
    "Lost Adventure's Armor": armor(250, 50, 30)
}

weapons = {
    "Wooden Sword": weapon(10, 3, 10, 50),
    "Shell Sword": weapon(20, 10, 30, 100),
    "Broken Dragon's sword": weapon(30, 20, 40, 150),
    "Dragon's sword": weapon(50, 20, 80, 250)
}

rooms = {
    "Start": Room(
        name="Raft",
        description="""You are stranded on a small raft, drifting aimlessly across an endless sea. 
The mist surrounds you, making it impossible to see more than a few feet ahead. 
The quiet sound of the waves is broken only by the occasional crash of thunder in the distance.""",
        loot={"Wooden Sword": "weapon", 
            "Leather Armor": "armor",
            "essence": "damage", 
            "coins": 50,
            "exp": 50},
        monster="Sea Serpent",
        connections={"north": "Beach", "east": "Lava Pit"}
    ),
    "Beach": Room(
        name="Beach",
        description="""The golden sand stretches before you as the warm sun beats down, the waves gently lapping at the shore. 
It's a peaceful place, but an ominous feeling lingers in the air, as if something dangerous is watching from the treeline.""",
        loot={"Shell Sword": "weapon", 
            "Healing Potion": 1,
            "essence": "crit chance", 
            "coins": 60,
            "exp": 100},
        monster="Crab King",
        connections={"south": "Start", "north": "Cavern", "west": "Merchant's Hut"}
    ),
    "Jungle": Room(
        name="Jungle",
        description="""The dense jungle is alive with the sounds of nature. 
Tall trees obscure the sun, casting deep shadows across the path. 
The air is thick with the scent of damp earth and the rustling of unseen creatures. 
Every step forward seems to draw you deeper into its mysterious heart.""",
        loot={
            "Jungle Armor": "armor",
            "Mana Potion": 1,
            "essence": "health", 
            "coins": 80,
            "exp": 100
        },
        monster="Jungle Tiger",
        puzzle="Solve a riddle to progress.",
        connections={"south": "Lava Pit", "north": "Temple"}
    ),
    "Merchant's Hut": Room(
        name="Merchant's Hut",
        description="""Nestled in a quiet corner of the island, a small hut sits surrounded by various trinkets and goods. 
Inside, the smell of incense and spices fills the air as a friendly merchant invites you to browse their selection of exotic items.""",
        loot={"gemstone": "Sapphire", 
            "exp": 150},
        monster=None,
        merchant=True,
        connections={"east": "Beach"}
    ),
    "Temple": Room(
        name="Temple",
        description="""An ancient stone temple rises from the jungle, its surface covered with vines and moss. 
A faint glow pulses from within, as if the building itself is alive with magic. 
The atmosphere is heavy with mystery and a sense of forgotten power.""",
        loot={"gemstone": "Ruby", 
            "key": "Secret Key",
            "exp": 200},
        monster="Golem Guardian",
        connections={"south": "Jungle", "north": "Mountain", "west": "Cavern"}
    ),
    "Mountain": Room(
        name="Mountain",
        description="""At the peak of a towering mountain, the cold, biting winds whip around you, carrying with them the scent of snow and ice. 
The landscape is harsh and unforgiving, but the view of the land below is breathtakingly beautiful. 
A sense of danger is palpable as you move deeper into the mountain’s heart.""",
        loot={"gemstone": "Jade", 
            "skill": "iron shield",
            "exp": 400},
        monster="Ice Dragon",
        connections={"south": "Temple", "west": "Hidden Cave", "north": "Lair"}
    ),
    "Hidden Cave": Room(
        name="Hidden Cave",
        description="""Tucked away beneath the mountain lies a dark and damp cave. 
The sound of dripping water echoes through the narrow tunnels. 
Glittering crystals line the walls, their faint glow lighting the way as strange, unexplainable noises stir in the shadows.""",
        loot={"essence": "crit damage", 
            "coins": "1000",
            "exp": 300},
        monster=None,
        puzzle="Solve the crystal alignment puzzle to access treasure.",
        requirement="Secret Key",
        connections={"east": "Mountain", "south": "Cavern"}
    ),
    "Cavern": Room(
        name="Cavern",
        description="""A dark, oppressive cavern stretches before you, the air thick with moisture and the scent of earth. 
The faint sounds of dripping water and echoing footsteps make it feel like you're not alone in this shadowy maze of stone.""",
        loot={"essence": "speed", 
            "coins": 200,
            "exp": 200},
        monster="Cave Bat",
        connections={"west": "Start", "east": "Lava Pit"}
    ),
    "Lava Pit": Room(
        name="Lava Pit",
        description="""The heat here is unbearable. A vast pit of bubbling lava stretches out before you, the air shimmering with its intense heat.
The smell of sulfur fills your nostrils as the ground trembles with the power of the flowing magma.""",
        loot={ "coins": 200,
            "exp": 500},
        monster="Fire Drake",
        puzzle="Find the safe path across the lava.",
        connections={"north": "Jungle", "west": "Start"}
    ),
    "Dragon's Lair": Room(
        name="Dragon's Lair",
        description="""The lair of the Dragon King is vast and intimidating. 
Treasure piles rise to the ceiling, glittering gold and precious gems scattered among the bones of fallen adventurers. 
The atmosphere is thick with the scent of smoke, and the presence of the dragon itself is felt in every corner of this vast cavern.""",
        loot="Victory",
        monster="Dragon King",
        connections={"south": "Mountain"}
    ),
}

def main():

    line()
    print("""After being stranded on a small raft in the middle of the ocean, you finally spot land in the distance.
Upon reaching the mainland, you discover an eerie island with a dangerous dungeon lurking beneath its surface. 
To survive, you must navigate its dark depths, battle fearsome monsters, and solve challenging puzzles, all while racing against time. 
Can you uncover the island's secrets and escape before it's too late?""")
    time.sleep(5)
    line()
    print("""You have 5 actions to choose from
1. Explore: explore the room, if the room is alr clear you can go ahead and enter a new room
2. Rest: Restore some amount of hp and mana
3. Inventory: Open your inventory
4. Upgrade: upgrade your stats
5. Stat: View your stat""")
    time.sleep(5)
    line()
    print("Get Ready get your name and start your journey!")
    username = input("Enter your name: ")
    player = Player(username, 100, 5, 50, 100, 40, 50, 5, 0)
    print(f"Welcome to the game {username}!\nChoose your action!")

    timer = 0  # Track the time in seconds

    while player.dead_count < 3 and timer <= 1800:

        if rooms["Dragon's Lair"].monster_defeated:
            print("You win the game\n Congratulations!!!!")
            break
        line()
        action = input("What will you do? (explore/rest/inventory/upgrade/stat): ").lower()
        if action == "explore":
            rooms[player.location].explore(player)
        elif action == "rest":
            print("You are resting this action take 10 seconds!")
            print("You rest and gain back 15% of hp and mana")
            player.rest()
        elif action == "upgrade":
            player.upgrade()
        elif action == "inventory":
            player.open_inventory()
        elif action == "stat":
            player.stats_view()

        if player.dead_count >= 3:
            print("Game Over")
            break

if __name__ == "__main__":
    main()
