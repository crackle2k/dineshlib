from engine import npc_speak, smart_input, gain_experience, add_item_to_inventory, enemy_speak, fight
from enemies import goblin

import random
import time
import sys
from colorama import init, Fore, Style

def battle_sequence():
    npc_speak("Willow", "It's time to start your first fight!")
    fight(goblin)
    