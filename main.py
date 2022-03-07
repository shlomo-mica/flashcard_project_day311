import tkinter as tk
from tkinter import PhotoImage

window = tk.Tk()

BACKGROUND_COLOR = "#B1DDC6"
window.title("FLASH CARD GAME")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
#front card
canvas = tk.Canvas(window, width=800, height=526)
photo = tk.PhotoImage(file="card_front.png")
canvas.create_image(400, 263, image=photo)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_text(400, 162, text="Title", font=("Ariel",20, "italic"))
canvas.create_text(400, 290, text="word", font=("Ariel", 40, "bold"))
canvas.grid(row=0,column=0,columnspan=2)
# buttons design
right_image = PhotoImage(file='right.png')
left_image = PhotoImage(file="wrong.png")

right_button = tk.Button(window, image=right_image, text="right", bg='pink', width=100,highlightthickness=0,background=BACKGROUND_COLOR)
right_button.grid(row=1,column=1)

left_button = tk.Button(image=left_image, text="left", bg='pink', width=100,highlightthickness=0,background=BACKGROUND_COLOR)
left_button.grid(row=1,column=0)

tk.mainloop()
