from sequences.intro import intro_sequence
from sequences.battle import battle_sequence
import tkinter as tk


def process_command(event=None):
    cmd = input_entry.get().strip()
    if cmd:
        display_message(f"> {cmd}")
        input_entry.delete(0, tk.END)
        run_command(cmd)

def display_message(message):
    output_box.insert(tk.END, message + "\n")
    output_box.see(tk.END)

def run_command(cmd):
    if cmd == "!exit":
        display_message("Goodbye.")
        window.destroy()
    else:
        display_message("Unknown command.")

def start_game():
    window = tk.Tk()
    window.title("Crimson Terminal")
    window.geometry("854x480")

    # Output area (read-only)
    output_box = tk.Text(window, height=20, bg="black", fg="red", font=("Consolas", 12))
    output_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    output_box.config(state=tk.DISABLED)

    # Input field
    input_entry = tk.Entry(window, font=("Consolas", 12), bg="gray15", fg="white", insertbackground="white")
    input_entry.pack(padx=10, pady=(0, 10), fill=tk.X)
    input_entry.bind("<Return>", process_command)
    input_entry.focus()

    # Unlock output for printing
    def display_message(message):
        output_box.config(state=tk.NORMAL)
        output_box.insert(tk.END, message + "\n")
        output_box.config(state=tk.DISABLED)
        output_box.see(tk.END)

    intro_sequence()
    battle_sequence()

    window.mainloop()



# if __name__ == "__main__":
    # intro_sequence()
    # battle_sequence()