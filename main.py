from tkinter import *
import random


BACKGROUND_COLOR = "#B1DDC6"
import pandas as pd
current_card={}
data=pd.read_csv("data/mal.csv")
to_learn=data.to_dict(orient="records")

def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(to_learn)
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_word,text=current_card["French"],fill="black")
    canvas.itemconfig(card_bg,image=front_img)
    flip_timer=window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title,text="Malayalam",fill="white")
    canvas.itemconfig(card_word,text=current_card["Malayalam"],fill="white")
    canvas.itemconfig(card_bg,image=back_img)

def is_known():
    to_learn.remove(current_card)
    next_card()

window = Tk()
window.title("FlashCard")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer=window.after(3000,func=flip_card)


canvas=Canvas(width=800,height=525)
front_img=PhotoImage(file="images/card_front.png")
back_img=PhotoImage(file="images/card_back.png")
card_bg=canvas.create_image(400,263,image=front_img)
card_title=canvas.create_text(400,149,text="",font=("Ariel",30,"italic"))
card_word=canvas.create_text(400,263,text="",font=("Ariel",45,"bold"))


canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)

cross_img=PhotoImage(file="images/wrong.png")
wrong_button=Button(image=cross_img,command=next_card)
wrong_button.grid(row=1,column=0)

tick_img=PhotoImage(file="images/right.png")
right_button=Button(image=tick_img,command=is_known)
right_button.grid(row=1,column=1)
next_card()

window.mainloop()
