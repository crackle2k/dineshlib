
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

def gain_experience(amount):
    global experience, level
    experience += amount

    while experience >= 100:
        experience -= 100
        level += 1
        print(Fore.GREEN + f"Level up! You are now Level {level}." + Fore.RESET)

def npc_speak(npc_name, message, delay=1.5):
    time.sleep(delay)
    print(Fore.YELLOW + "[NPC] " + Fore.RESET + f"{npc_name}: {message}")

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
        print(f"Level: {level}, XP: {experience}/100")
    elif cmd == "!help":
        print("Available commands: !hotbar, !inventory, !level, !help")
    else:
        print("Unknown command.")


inventory = {}  # Infinite Inventory
hotbar = [None] * 9  # 9 Initially Empty Slots

def add_item_to_inventory(item, amount=1):
    inventory[item] = inventory.get(item, 0) + amount
    print(Fore.CYAN + f"You received {amount}x {item}." + Style.RESET_ALL)
    assign_to_hotbar(item)

def assign_to_hotbar(item):
    print(f"Would you like to assign {item} to a hotbar slot (1–9)?")
    show_hotbar()
    
    try:
        slot_input = smart_input("Enter slot number (1–9), or 0 to skip: ")
        slot = int(slot_input)
        if 1 <= slot <= 9:
            hotbar[slot - 1] = item
            print(Fore.YELLOW + f"{item} assigned to slot {slot}." + Style.RESET_ALL)
        elif slot == 0:
            print("Skipped hotbar assignment.")
        else:
            print("Invalid slot.")
    except ValueError:
        print("Invalid input. Skipping.")

def show_hotbar():
    print(Fore.LIGHTMAGENTA_EX + "\n--- Hotbar ---" + Style.RESET_ALL)
    for i, item in enumerate(hotbar, 1):
        item_display = item if item else "Empty"
        print(f"{i}. {item_display}")

def show_inventory():
    print(Fore.LIGHTCYAN_EX + "\n--- Inventory ---" + Style.RESET_ALL)

    if not inventory:
        print("Your inventory is empty.")
        return

    for item, amount in inventory.items():
        print(f"{item} x{amount}")