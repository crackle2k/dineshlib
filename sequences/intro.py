from engine import npc_speak, smart_input, gain_experience, add_item_to_inventory

import random
import time
import sys
from colorama import init, Fore, Style

def intro_sequence():
    print("Press Enter To Start")

    start = input()

    if start == "":
        print("Welcome To The Terminal.")
    else:
        print("Welcome To The Terminal.")

    time.sleep(0.5)

    name = smart_input("Please enter your name: ")
    npc_speak("?", f"Hello {name}.")



    npc_speak("?", "You have entered the world of Sanguine.")
    npc_speak("?", "The year is currently 1649.")
    npc_speak("?", "Your goal is to survive as long as you can.")
    npc_speak("Willow", "My name is Willow.")
    npc_speak("Willow", "I don't have long.")
    npc_speak("Willow", "I need you to keep going.")
    npc_speak("Willow", "And never, under any circumstances, stop.")


    initialContinue = smart_input("Continue? ").lower()

    if initialContinue in ["yes", "y", "sure", "ok", "continue"]:
        print("Very well.")
    else:
        print("*Sigh...* Alright.")
        sys.exit()

    print(Fore.GREEN + "You've gained 100 XP!" + Fore.RESET)
    gain_experience(100)

    time.sleep(0.5)

    npc_speak("Willow", "In Sanguine, things work a little bit... different.")
    npc_speak("Willow", "There are creatures here that have proven to be a little unsettling.")
    npc_speak("Willow", "I'm going to give you a sword, which I hope can help get you started.")

    add_item_to_inventory("Willow's Rusty Blade")

    npc_speak("Willow", "Nice! This should get you set up.")