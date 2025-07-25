from sequences.intro import intro_sequence
from sequences.battle import battle_sequence
import tkinter as tk

window = tk.Tk()
window.title("Fullscreen Window")
window.geometry("854x480")

label = tk.Label(window, text="Hello, World!", font=("Arial", 16))
label.pack(pady=20)

window.mainloop()


# if __name__ == "__main__":
    # intro_sequence()
    # battle_sequence()