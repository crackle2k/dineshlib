class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name, quantity=1):
        self.items[name] = self.items.get(name, 0) + quantity
        return f"👜 Added {quantity}x {name} to your inventory."

    def remove_item(self, name, quantity=1):
        if name in self.items:
            self.items[name] -= quantity
            if self.items[name] <= 0:
                del self.items[name]
            return f"❌ Removed {quantity}x {name}."
        return f"⚠ You do not have {name}."

    def list_items(self):
        if not self.items:
            return "📦 Inventory is empty."
        return "\n".join([f"{item} x{qty}" for item, qty in self.items.items()])
