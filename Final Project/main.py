import random
import time
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def line():
    print("---------------------------------------------------------------------------")
class Player:
    def __init__(self, name, health, endurance, speed, mana, damage, crit_damage, crit_chance):
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
        self.coins = 0
        self.weapon = None
        self.armor = None
        self.inventory = {
            "healing potion": 0,
            "mana potion": 0
        }
        self.dead_count = 0
        self.location = "Raft"
        self.previous_location = "Raft"
        self.level = 0
        self.exp = 0
        self.upgrade_points = 0
        self.coins = 0
        self.skills = {
            "slash": {"mana": 0, "damage": 20},
            "fire": {"mana": 35, "damage": 50},
            "stunt": {"mana": 30, "damage": 10},
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
        self.health = self.max_health
        
    def rest(self):
        line()
        self.heal(self.max_health*0.15)
        self.mana_regen(self.max_mana*0.15)
        time.sleep(5)
    
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
        if skill == "stunt":
            damage_dealt = self.skills[skill]["damage"]
            print(f"You deal {damage_dealt} damage")
            self.mana -= self.skills[skill]["mana"]
            return damage_dealt          
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
        if item == "coins":
            self.coins += types
            return
        elif item == "exp":
            self.earn_exp(types)
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
            if self.armor != None:
                if armors[item].level > armors[self.armor].level:
                    self.change_armor(item)
                    self.armor = item
                else:
                    line()
                    print("You already have higher level armor equiq")
                    return
            self.change_armor(item)
            self.armor = item

        elif types == "weapon":
            if self.weapon != None:
                if weapons[item].level > weapons[self.weapon].level:
                    self.weapon = item
                    self.max_mana += weapons[item].mana
                else:
                    line()
                    print("You already have higher level armor equiq")
            self.weapon = item
        elif types == "special":
            self.damage *= 2
            self.max_health *= 2
            self.health = self.max_health

    def stats_view(self):
        line()
        print("This is your current stats")
        print(f"Level: {self.level}")
        print(f"exp: {self.exp}/100")
        print(f"Max Health: {self.max_health}")
        print(f"Current Health {self.health}")
        print(f"Endurance: {self.endurance}")
        print(f"Max Mana: {self.max_mana}")
        print(f"Current Mana: {self.mana}")
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
        line()
        print(f"6. Upgrade Armor: {self.armor}")
        print(f"7. Upgrade Weapon: {self.weapon}")        

        try:
            stat = int(input("Enter number of stats to upgrade: "))
        except ValueError:
            print("Please enter an integers!")
            return
        if stat not in range(1, 8):
            print("Please Enter number beetween 1-7") 
            return
        elif stat in range(1, 6):
            try:
                upgrade_point = int(input("Enter amount of upgrade points to use: "))
            except ValueError:
                print("Please enter an integer")
                return
            if upgrade_point > self.upgrade_points or upgrade_point < 0:
                print("Please Enter valid amount of upgrade points")
                return

        match stat:
            case 1:
                upgrade = 10*upgrade_point
                print(f"Your max health increase by {upgrade}")
                self.max_health += upgrade
                self.upgrade_points -= upgrade_point
                print(f"You are left with {self.upgrade_points} upgrade points")
            case 2:
                upgrade = 10*upgrade_point
                print(f"Your max mana increase by {upgrade}")
                self.max_mana += upgrade
                self.upgrade_points -= upgrade_point
                print(f"You are left with {self.upgrade_points} upgrade points")
            case 3:
                upgrade = 5*upgrade_point
                print(f"Your damage increase by {upgrade}")
                self.damage += upgrade
                self.upgrade_points -= upgrade_point
                print(f"You are left with {self.upgrade_points} upgrade points")
            case 4:
                upgrade = 2*upgrade_point
                print(f"Your critical chance increase by {upgrade}")
                self.crit_chance += upgrade
                self.upgrade_points -= upgrade_point
                print(f"You are left with {self.upgrade_points} upgrade points")
            case 5:
                upgrade = 11*upgrade_point
                print(f"Your critical damage increase by {upgrade}")
                self.crit_damage += upgrade
                self.upgrade_points -= upgrade_point
                print(f"You are left with {self.upgrade_points} upgrade points")
            case 6:
                gemstone = input("Enter gemstone to upgrade your armor (this action cannot be reverse): ")
                if gemstone in self.inventory.keys():
                    armors[self.armor].upgrade(gemstone)
                else:
                    print("Please enter valid gemstones")
            case 7:
                gemstone = input("Enter gemstone to upgrade your weapon (this action cannot be reverse): ")
                if gemstone in self.inventory.keys():
                    weapons[self.weapon].upgrade(gemstone)
                else:
                    print("Please enter valid gemstones")


    def earn_exp(self, points):
        self.exp += points
        if self.exp >= 100:
            self.upgrade_points += (int(self.exp/100)) * 5
            self.level += int(self.exp/100)
            self.exp = self.exp % 100
            line()
            print(f"You leveled up level")
            print(f"Your hp and mana reset!")
            line()
            self.mana = self.max_mana
            self.health = self.max_health

    def use_item(self, item):
        if item in self.inventory and self.inventory[item] > 0:
            self.inventory.remove(item)
            if item == "Healing Potion":
                self.heal(30)
            elif item == "Mana Potion":
                self.mana_regen(20)
            print(f"Used {item}")
            return True
        else:
            print("Item unavailabe")
            return False

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
            "broken dragon's sword": {"types": "weapon", "prices": 100},
            "lost adventure's armor": {"types": "armor", "prices": 400},
            "healing Potion": {"types": "potion", "prices": 30},
            "mana potion": {"types": "potion", "prices": 30},
            "love leterr???": {"types": "special", "prices": 1000}
        }


    def explore(self, player):
        line()
        print(f"You are in the {self.name}")
        print(self.description)
        self.visited = True
        
        if self.monster != None and not self.monster_defeated:
            self.combat(player)
        elif self.puzzle and not self.puzzle_fail:
            print("You encounter a puzzle from the ancient age. You got one try")
            if self.solve_puzzle():
                print("You gain 50 coins and 150 exp for solving the puzzle!")
                player.coins += 50
                player.gain_exp(150)
            else:
                self.puzzle_fail = True
        elif self.merchant:
            print("You found merchant!")
            choice = input("Do you want to interact with him (y/n): ").lower()
            if choice == "y":
                self.interact_with_merchant(player)
        elif self.merchant:
            line()
            print('Merchant: "comeback again if you interest in our goods!"')
            line()
        else:
            line()
            print("You have explored everything in this rooms! Travel to the next room using 'travel'")

    def travel(self, player):
        while True:
            if not self.monster_defeated and player.location == "Raft":
                print("You must defeat monster first in this room")
                return
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
                break
            else:
                line()
                print("Invalid direction. Try again.")
                continue

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
                    if player.mana - player.skills[choose_skill]["mana"] < 0:
                        print("Not enough mana\nChoose skill again!!!")
                        continue
                    if choose_skill == "stunt":
                        monsters[self.monster].health -= player.attack(choose_skill)
                        if random.random() < 60.0/100.0:
                            print("You stunt the monster!")
                            continue
                        else:
                            print("You failed to stunt the monster...")
                            break
                    else:
                        monsters[self.monster].health -= player.attack(choose_skill)
                        break
            elif action == "potion":
                while True:
                    line()
                    print("Potions in inventory:")
                    for potion, amount in player.inventory.items():
                        print(f"{potion}: {amount}")
                    item = input("Which potion do you want to use? (Enter to skip this action): ").lower()
                    if action != ["healing potion", "mana potion"]:
                        ("You done nothing...")
                        break
                    if not player.use_item(item):
                        continue

            elif action == "escape":
                line()
                if self.name == "Raft":
                    print("You can't escape from this room!")
                else:
                    print(f"You back in to the {player.previous_location}")
                    player.location = player.previous_location
                    return

            if monsters[self.monster].health > 0:
                player.take_damage(self.monster)

        if player.health <= 0:
            player.dead_count += 1
            line()
            print(f"You were defeated by the {self.monster}")
            print(f"You respawwn in to the {player.previous_location}")
            print(f"You have {2 - player.dead_count} life left")
            player.location = player.previous_location
            line()
            return
        else:
            line()
            print(f"You defeated the {self.monster}")
            line()
            self.monster_defeated = True
        
        if self.loot and not self.item_picked_up and self.monster_defeated:
            line()
            print("You get rewards for killing monster:")
            for item, types in self.loot.items():
                print(f"{item}: {types}")
                player.add_to_inventory(types, item)
            self.item_picked_up = True
            line()

    def solve_puzzle(self):

        if self.name == "Lava Pit":
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

        if self.name == "Jungle":

            correct_sequence = "CEGDA"

            print("Clue:")
            print("\"Nature’s melody unlocks the way,\nFollow the rhythm the jungle plays.\"")
            print("Listen carefully to the bird calls and reproduce the melody.")
            print("Character arE Going Down the Aisle!")

            user_sequence = input("Enter the note (no space)(C, D, E, G, A): ").capitalize()

            if user_sequence != correct_sequence:
                print("The vines tighten! You've chosen incorrectly. Resetting...")
                return False

            print("The vines part, revealing a hidden path!")
            return True
        
        if self.name == "Hidden Cave":
            print("Clue:")
            print("\"Reflect the truth, dispel the lies,\nAlign the crystals where light complies.\nThe key lies where red and blue collide.\"")

            print("You see crystals: Red, Blue, Green, Yellow. Choose two to place.")

            first = input("Choose the first crystal to place: ").capitalize()
            second = input("Choose the second crystal to place: ").capitalize()

            if first == "Red" and second == "Blue" or first == "Blue" and second == "Red":
                print("The beams of light converge into a purple glow. The pedestal activates!")
                return True
            else:
                print("The crystals fail to align. Try again.")
                return False


    def interact_with_merchant(self, player):

        line()
        print(f"You have {player.coins} coins")
        print("Merchant offers the following items for sale:")

        for item in self.merchant_item.keys():
            print(f"{item}: {self.merchant_item[item]["prices"]} coins")
        line()

        item_to_buy = input("Which item would you like to buy? ").lower()

        if item_to_buy in self.merchant_item.keys():
            if self.merchant_item[item_to_buy]["types"] == "potion":
                line()
                while True:
                    try:
                        amount = int(input("Enter amount of potions you want to buy: "))
                        break
                    except ValueError:
                        print("Please Enter integer amount!")
                        continue

                if player.coins < self.merchant_item[item_to_buy]["prices"] * amount:
                    print("Not enough coins!")
                    user_choice = input("Do you want to interact again? (1 for yes, any key for no): ")
                    if user_choice == "1":
                        self.interact_with_merchant(player)
                    return
                else:
                    prices = self.merchant_item[item_to_buy]["prices"] * amount
            else:
                prices = self.merchant_item[item_to_buy]["prices"]
                
            player.coins -= prices
            player.add_to_inventory(self.merchant_item[item_to_buy]["types"], item_to_buy)
            print(f"Item {item_to_buy} purchased.")
        else:
            print("Item unavailable.")

        user_choice = input("Do you want to interact again? (1 for yes, any key for no): ")
        if user_choice == "1":
            self.interact_with_merchant(player)

class weapon:
    def __init__(self, damage, crit_chance, crit_damage, mana, level):
        self.damage = damage
        self.crit_chance = crit_chance
        self.crit_damage = crit_damage
        self.mana = mana
        self.level = level

    
    def upgrade(self, gemstone):
        if gemstone == "Ruby":
            self.crit_damage += 40
        elif gemstone == "Sapphire":
            self.mana += 50
        elif gemstone == "Jade":
            self.crit_chance += 10
        print(f"Upgraded weapon with {gemstone}")
class armor:
    def __init__(self, health, endurance, speed, level):
        self.health = health
        self.endurance = endurance
        self.speed = speed
        self.level = level

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
    "Crab King": Monster("Crab King", 550, 10, 30, 25),
    "Jungle Tiger": Monster("Jungle Tiger", 600, 15, 55, 30),
    "Golem Guardian": Monster("Golem Guardian", 1000, 20, 20, 5),
    "Ice Dragon": Monster("Ice Dragon", 1200, 40, 80, 30),
    "Cave Bat": Monster("Cave Bat", 650, 10, 45, 50),
    "Fire Drake": Monster("Fire Drake", 600, 40, 40, 30),
    "Dragon King": Monster("Dragon King", 2800, 60, 200, 60),
}

armors = {
    "Leather Armor": armor(50, 10, 5, 1),
    "Jungle Armor": armor(100, 20, 15, 2),
    "Lost Adventure's Armor": armor(250, 50, 30, 3)
}

weapons = {
    "Wooden Sword": weapon(10, 3, 10, 50, 1),
    "Shell Sword": weapon(20, 10, 30, 100, 2),
    "Broken Dragon's sword": weapon(30, 20, 40, 150, 3),
    "Dragon's sword": weapon(50, 20, 80, 250, 4)
}

rooms = {
    "Raft": Room(
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
        connections={"south": "Raft", "north": "Cavern", "west": "Merchant's Hut"}
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
        connections={"west": "Raft", "east": "Lava Pit"}
    ),
    "Lava Pit": Room(
        name="Lava Pit",
        description="""The heat here is unbearable. A vast pit of bubbling lava stretches out before you, the air shimmering with its intense heat.
The smell of sulfur fills your nostrils as the ground trembles with the power of the flowing magma.""",
        loot={ "coins": 200,
            "exp": 500},
        monster="Fire Drake",
        puzzle="Find the safe path across the lava.",
        connections={"north": "Jungle", "west": "Raft"}
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
    time.sleep(3)
    line()
    print("""You have 6 actions to choose from
1. Explore: explore the room, if the room is alr clear you can go ahead and enter a new room
2. Travel: Travel to another room by selecting (North/South/East/West)
3. Rest: Restore some amount of hp and mana
4. Inventory: Open your inventory
5. Upgrade: upgrade your stats
6. Stat: View your stat""")
    time.sleep(3)
    line()
    print("You have 20 minutes to finish the game\nGet Ready get your name and start your journey!")
    username = input("Enter your name: ")
    player = Player(username, 100, 0, 5, 100, 50, 50, 5)
    print(f"Welcome to the game {username}!\nChoose your action!")

    while player.dead_count < 3:

        start_time = time.time()
        time_limit = 20 * 60  

        elapsed_time = time.time() - start_time
        if elapsed_time >= time_limit:
            break

        if rooms["Dragon's Lair"].monster_defeated:
            print("You win the game\n Congratulations!!!!")
            break
        line()
        action = input("What will you do? (explore/travel/rest/inventory/upgrade/stat): ").lower()
        if action == "explore":
            rooms[player.location].explore(player)
        elif action == "rest":
            line()
            print("You are resting this action take 5 seconds!")
            print("You rest and gain back 15% of hp and mana")
            player.rest()
        elif action == "upgrade":
            player.upgrade()
        elif action == "inventory":
            player.open_inventory()
        elif action == "stat":
            player.stats_view()
        elif action == "travel":
            rooms[player.location].travel(player)

        if player.dead_count >= 3:
            print("Game Over")
            break

if __name__ == "__main__":
    main()