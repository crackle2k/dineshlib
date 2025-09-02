class Player:
    def __init__(self, name="Hero", health=100, coins=0, level=1):
        self.name = name
        self.health = health
        self.coins = coins
        self.level = level

    def add_coins(self, amount):
        self.coins += amount
        return f"💰 Gained {amount} coins. Total: {self.coins}"

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.health = 0
            return "☠ You have fallen in battle."
        return f"❤️ Health: {self.health}"

    def heal(self, amount):
        self.health += amount
        return f"❤️ Healed {amount}. Health: {self.health}"

    def level_up(self):
        self.level += 1
        return f"🏆 Level Up! You are now level {self.level}."
