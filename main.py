import tkinter as tk
from tkinter import scrolledtext
import time
import threading

# --- Synapse Medieval Terminal ---
class SynapseTerminal:
    def __init__(self, master):
        self.master = master
        self.master.title("Synapse Terminal")
        self.master.configure(bg="#f5deb3")  # parchment color

        # Medieval font setup
        self.font = ("Papyrus", 14)  # Change if you want another medieval font

        # Scrollable output box
        self.output = scrolledtext.ScrolledText(
            master, wrap=tk.WORD, width=60, height=20,
            bg="#f5deb3", fg="#4b2e2e", font=self.font
        )
        self.output.pack(padx=10, pady=10)
        self.output.config(state=tk.DISABLED)

        # Command entry box (disabled at start until boot finishes)
        self.entry = tk.Entry(
            master, width=60, bg="#f5deb3", fg="#4b2e2e", font=self.font
        )
        self.entry.pack(padx=10, pady=5)
        self.entry.bind("<Return>", self.run_command)
        self.entry.config(state=tk.DISABLED)

        # Command dictionary
        self.commands = {
            "!help": self.cmd_help,
            "!about": self.cmd_about,
            "!clear": self.cmd_clear
        }

        # Start boot animation
        threading.Thread(target=self.boot_sequence, daemon=True).start()

    def boot_sequence(self):
        boot_lines = [
            "⚜ Initializing Synapse Core...",
            "📜 Loading ancient scrolls of wisdom...",
            "🔮 Binding thought to spellcraft...",
            "🏰 Forging neural pathways of the realm...",
            "✨ Synapse is now awakened."
        ]
        self.output.config(state=tk.NORMAL)
        for line in boot_lines:
            self.output.insert(tk.END, line + "\n")
            self.output.see(tk.END)
            time.sleep(1)  # delay between lines for animation
        self.output.insert(tk.END, "\nType !help to begin your quest.\n")
        self.output.config(state=tk.DISABLED)

        # Enable input after boot
        self.entry.config(state=tk.NORMAL)

    def run_command(self, event=None):
        cmd = self.entry.get().strip()
        self.entry.delete(0, tk.END)

        self.output.config(state=tk.NORMAL)
        self.output.insert(tk.END, f"\n> {cmd}\n")

        if cmd in self.commands:
            response = self.commands[cmd]()
            self.output.insert(tk.END, response + "\n")
        else:
            self.output.insert(tk.END, "⚠ The Synapse cannot comprehend this incantation.\n")

        self.output.config(state=tk.DISABLED)
        self.output.see(tk.END)

    def cmd_help(self):
        return "📜 Commands: !help, !about, !clear"

    def cmd_about(self):
        return "🏰 Synapse Terminal — An ancient interface where mind meets magic."

    def cmd_clear(self):
        self.output.delete(1.0, tk.END)
        return "The scroll hath been cleansed."
    
    def write_output(self, text):
        self.output.config(state=tk.NORMAL)
        self.output.insert(tk.END, text + "\n")
        self.output.see(tk.END)
        self.output.config(state=tk.DISABLED)




# --- Main Program ---
if __name__ == "__main__":
    root = tk.Tk()
    app = SynapseTerminal(root)
    root.mainloop()
