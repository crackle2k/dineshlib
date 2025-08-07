import tkinter as tk

def run_command(cmd):
    cmd = cmd.lower()  # Normalize the command

    if cmd == "!exit":
        display_message("Goodbye.")
        window.after(1000, window.destroy)
    elif cmd == "!help":
        display_message("Available commands: !help, !exit, !about")
    elif cmd == "!about":
        display_message("Synapse Terminal v1.0 - A story-driven text RPG in your own terminal.")
    else:
        display_message("Unknown command. Type !help for options.")


def display_message(message):
    output_box.config(state=tk.NORMAL)
    output_box.insert(tk.END, message + "\n")
    output_box.config(state=tk.DISABLED)
    output_box.see(tk.END)

# --- Create the GUI window ---
window = tk.Tk()
window.title("Synapse")
window.geometry("854x480")
window.configure(bg="black")

# --- Output Text Box (read-only) ---
output_box = tk.Text(
    window,
    bg="black",
    fg="red",
    font=("Consolas", 12),
    insertbackground="white"
)
output_box.pack(padx=10, pady=(10, 0), fill=tk.BOTH, expand=True)
output_box.config(state=tk.DISABLED)

# --- Input Entry Field ---
input_entry = tk.Entry(
    window,
    bg="gray15",
    fg="white",
    font=("Consolas", 12),
    insertbackground="white"
)
input_entry.pack(padx=10, pady=10, fill=tk.X)
input_entry.bind("<Return>", run_command)
input_entry.focus()

# --- Welcome Message ---
display_message("Welcome to Synapse Terminal. Type !help to get started.")

# --- Start the GUI loop ---
window.mainloop()
