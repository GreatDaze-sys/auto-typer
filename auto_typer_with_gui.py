import time
import tkinter as tk

def auto_type(text, typing_speed=0.05):
    for char in text:
        text_widget.insert("end", char)
        text_widget.see("end")
        text_widget.update()
        time.sleep(typing_speed)

def start_typing():
    text = text_entry.get()
    typing_speed = float(speed_entry.get())
    auto_type(text, typing_speed)

root = tk.Tk()
root.title("Auto Typer")

text_label = tk.Label(root, text="Text:")
text_entry = tk.Entry(root)

speed_label = tk.Label(root, text="Typing Speed (s):")
speed_entry = tk.Entry(root, width=5)
speed_entry.insert(0, "0.05")

start_button = tk.Button(root, text="Start Typing", command=start_typing)

text_widget = tk.Text(root, height=10, width=50)

text_label.pack()
text_entry.pack()
speed_label.pack()
speed_entry.pack()
start_button.pack()
text_widget.pack()

root.mainloop()
