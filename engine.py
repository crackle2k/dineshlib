
import random
import time
import sys
from colorama import init, Fore, Style

# Crimson Terminal

health = 100
experience = 0
level = 0
hunger = 100
gold = 0
mana = 100
defense = 0

def gain_experience(amount):
    global experience, level
    experience += amount

    while experience >= 100:
        experience -= 100
        level += 1
        display_message(Fore.GREEN + f"Level up! You are now Level {level}." + Fore.RESET)

def npc_speak(npc_name, message, delay=1.5):
    time.sleep(delay)
    display_message(Fore.YELLOW + "[NPC] " + Fore.RESET + f"{npc_name}: {message}")

def enemy_speak(enemy_name, message, delay=1.5):
    time.sleep(delay)
    display_message(Fore.RED + "[ENEMY] " + Fore.RESET + f"{enemy_name}: {message}")

def smart_input(prompt):
    while True:
        user_input = input(prompt).strip()

        if user_input.startswith("!"):
            handle_global_command(user_input.lower())
            continue  # ask again after command
        else:
            return user_input

def handle_global_command(cmd):
    if cmd == "!hotbar":
        show_hotbar()
    elif cmd == "!inventory":
        show_inventory()
    elif cmd == "!level":
        display_message(f"Level: {level}, XP: {experience}/100")
    elif cmd == "!help":
        display_message("Available commands: !hotbar, !inventory, !level, !help")
    elif cmd == "!hunger":
        display_message(f"Hunger: {hunger}")
    else:
        display_message("Unknown command.")


inventory = {}  # Infinite Inventory
hotbar = [None] * 9  # 9 Initially Empty Slots

def add_item_to_inventory(item, amount=1):
    inventory[item] = inventory.get(item, 0) + amount
    display_message(Fore.CYAN + f"You received {amount}x {item}." + Style.RESET_ALL)
    assign_to_hotbar(item)

def assign_to_hotbar(item):
    display_message(f"Would you like to assign {item} to a hotbar slot (1–9)?")
    show_hotbar()
    
    try:
        slot_input = smart_input("Enter slot number (1–9), or 0 to skip: ")
        slot = int(slot_input)
        if 1 <= slot <= 9:
            hotbar[slot - 1] = item
            display_message(Fore.YELLOW + f"{item} assigned to slot {slot}." + Style.RESET_ALL)
        elif slot == 0:
            display_message("Skipped hotbar assignment.")
        else:
            display_message("Invalid slot.")
    except ValueError:
        display_message("Invalid input. Skipping.")

def change_hunger(amount):
    global hunger
    hunger = max(0, hunger + amount)





def show_hotbar():
    display_message(Fore.LIGHTMAGENTA_EX + "\n--- Hotbar ---" + Style.RESET_ALL)
    for i, item in enumerate(hotbar, 1):
        item_display = item if item else "Empty"
        display_message(f"{i}. {item_display}")

def show_inventory():
    display_message(Fore.LIGHTCYAN_EX + "\n--- Inventory ---" + Style.RESET_ALL)

    if not inventory:
        display_message("Your inventory is empty.")
        return

    for item, amount in inventory.items():
        display_message(f"{item} x{amount}")






def fight(enemy):
    global health, hunger

    display_message(f"\nA wild {enemy['name']} appears!")
    display_message(f"{enemy['name']} HP: {enemy['health']}")

    while enemy["health"] > 0 and health > 0:
        display_message(f"\nYour HP: {health} | Hunger: {hunger}")
        action = smart_input("Do you want to [attack], [run], or [status]? ").lower()

        if action == "attack":
            dmg = random.randint(8, 15)
            enemy["health"] -= dmg
            display_message(f"You strike the {enemy['name']} for {dmg} damage!")

            if enemy["health"] <= 0:
                display_message(f"You defeated the {enemy['name']}!")
                break

            # Enemy turn
            enemy_dmg = random.randint(5, enemy["attack"])
            health -= enemy_dmg
            display_message(f"The {enemy['name']} hits you for {enemy_dmg} damage!")

            change_hunger(-5)  # Hunger drops per turn

        elif action == "run":
            display_message("You ran away!")
            break

        elif action == "status":
            display_message(f"HP: {health}, Hunger: {hunger}")

        else:
            display_message("Invalid action.")

    if health <= 0:
        display_message(Fore.RED + "You have been defeated..." + Fore.RESET)
        sys.exit()
