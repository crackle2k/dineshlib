class NPC:
    def __init__(self, name, terminal=None):
        self.name = name
        self.dialogue = []
        self.terminal = terminal  # store reference to SynapseTerminal

    def add_dialogue(self, line):
        self.dialogue.append(line)

    def talk(self):
        if not self.dialogue:
            self._say(f"{self.name} has nothing to say.")
        else:
            for line in self.dialogue:
                self._say(f"{self.name}: {line}")

    def _say(self, text):
        if self.terminal:
            self.terminal.write_output(text)
        else:
            print(text)  # fallback if no terminal is connected

self.elder = NPC("Elder Rowan", terminal=self)
self.elder.add_dialogue("Greetings, traveler. Beware the dark forest.")
self.elder.add_dialogue("Legends speak of a hidden treasure beyond the hills.")
