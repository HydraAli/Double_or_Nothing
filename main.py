from cProfile import label
from glob import glob
import sys
from tkinter import*
# from PIL import ImageTk, Image
from random import randint

window = Tk()
window.geometry("1366x768")
frame = Frame(window)
frame.pack(side="top", expand=True, fill="both")
window.title("DOUBLE or NOTHING")
# img = ImageTk.PhotoImage(Image.open("E:\\MY PROGRAMS\\DN bg img.jpg"))  # <-- PIL
canv = Canvas(master=window)
# frk = Label(frame, image=img)
# frk.pack()
points = int(0)

def Odd():
    clear()
    global ki
    if rand%2!=0:
        global points
        label = Label(frame, text="You got it ", fg='black', bg='red', font=(20))
        label.place(relx=0.5, rely=0.3, anchor=CENTER)
        points += 100
    else:
        label = Label(frame, text="You didn't got it")
        label.place(relx=0.5, rely=0.3, anchor=CENTER)
        global ls
        points = 0
        ls = points
        ki = ls
    label2 = Label(frame, text=f"Last score : {ki}")
    label2.place(relx=0.5, rely=0.9, anchor=CENTER)
    label1 = Label(frame, text=f"Points: {points}", fg='black', bg='green',font=('Central',35, 'bold'))
    label1.place(relx=0.5, rely=0.7, anchor=CENTER)
    if points >= 1000:
        clearf()
def Even():
    clear()
    global ki
    if rand%2==0:
        global points
        label = Label(frame, text="You got it ", fg='black', bg='red', font=(20))
        label.place(relx=0.5, rely=0.3, anchor=CENTER)
        points += 100
    else:
        label = Label(frame, text="You didn't got it")
        label.place(relx=0.5, rely=0.3, anchor=CENTER)
        global ls
        points = 0
        ls = points
        ki = ls
    label2 = Label(frame, text=f"Last score : {ki}")
    label2.place(relx=0.5, rely=0.9, anchor=CENTER)
    label1 = Label(frame, text=f"Points: {points}", fg='black', bg='green',font=('Central',35, 'bold'))
    label1.place(relx=0.5, rely=0.7, anchor=CENTER)
    if points >= 1000:
        clearf()
def exit():
        sys.exit()
def clearf():
    for widgets in frame.winfo_children():
      widgets.destroy()
    label = Label(frame, text="The odds of this happening are 0.0009765625%", bg='black', fg='white', font=('Central', 30, 'bold'))
    label.place(relx=0.5, rely=0.3, anchor=CENTER)
    win = Label(frame, text="YOU WON", fg = 'black', bg= 'green', font=('Central', 50, ' bold'))
    win.place(relx=0.5, rely= 0.5, anchor=CENTER)
    button = Button(frame, text="EXIT", bg='red', fg='white', font=('Central', 20,'bold'), command=exit)
    button.place(relx=0.5, rely=0.92, anchor=CENTER)
def clear():
    global points
    window.attributes('-fullscreen', True)
    global hs
    global rand
    global z
    try:
        if points > hs:
            hs = points
    except:
        hs = 0
    z = 0
    rand = randint(1,100)
    for widgets in frame.winfo_children():
      widgets.destroy()
    label = Label(frame, text="Guess either the result is HEADS or TAILS", fg='White', bg='Black', font=('Central',20, 'bold'))
    label.place(relx=0.5, rely=0.09, anchor=CENTER)
    odd = Button(frame, text="HEADS", fg='white', relief='flat',bg='black', font=('Central',35, 'bold'), command=Odd)
    odd.place(relx=0.4,rely=0.5,anchor=CENTER)
    even = Button(frame, text="TAILS", fg='black', relief='flat',bg='white', font=('Central',35, 'bold'), command=Even)
    even.place(relx=0.6,rely=0.5,anchor=CENTER)
    fs = Button(frame, text="X", relief='groove', bg='red', fg='black', font=('Central', 10,'bold'), command=exit)
    fs.place(relx=0.99, rely=0.01, anchor=CENTER)
    label2 = Label(frame, text=f"High score: {hs}", bg='yellow', fg='black', font=('Central', 30,'bold'))
    label2.place(relx=0.5, rely=0.03, anchor=CENTER)
def __init__(self):
    print(hs)
if __name__ == "__main__":
    rand = randint(1,100)
    label = Label(frame, text="Double or Nothing", fg='White', bg='Black', font=('Central',20, 'bold'))
    label.place(relx=0.5, rely=0.07, anchor=CENTER)
    label = Label(frame, text="Hello Wanna Test your luck?\n In this game we will toss a coin and you will have to\nGuess either the result is Heads or Tails\n If you get it right your points will be increased by 100 and if you lose your all points will be deducted", fg='white', bg='black', font=('Central',15, 'bold'))
    label.place(relx=0.5, rely=0.2, anchor=CENTER)
    bs = Button(frame, text="Start", fg='black', relief='flat',bg='Blue', font=('Central',35, 'bold'), command=clear)
    bs.place(relx=0.5, rely=0.8, anchor=CENTER)
    mainloop()
