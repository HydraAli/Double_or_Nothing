import sys
from tkinter import*
from tkinter import ttk
import tkinter
from PIL import ImageTk, Image
from random import randint
from playsound import playsound

window = Tk()
window.geometry("1366x768")
frame = Frame(window)
frame.pack(side="top", expand=True, fill="both")
window.title("DOUBLE or NOTHING")
canv = Canvas(master=window)
img = ImageTk.PhotoImage(Image.open("E:\\MY PROGRAMS\\Double or Nothing\\Double or Nothing\\Double or Nothing bg(4.0).png"))  # <-- PIL
img2 = ImageTk.PhotoImage(Image.open("E:\\MY PROGRAMS\\Double or Nothing\\Double or Nothing\\Win bg.png")) 
img3 = ImageTk.PhotoImage(Image.open("E:\\MY PROGRAMS\\Double or Nothing\\Double or Nothing\\settings bg.png"))  
img4 = ImageTk.PhotoImage(Image.open("E:\\MY PROGRAMS\\Double or Nothing\\Double or Nothing\\main bg.png")) 
points = int(0)
muted = False
win_score = 1000
play = playsound
def message(text):
    mesg = Label(frame, text=text, fg='black', bg='grey',font=('Cursive',20, 'bold'), borderwidth=2)
    mesg.place(relx = 0.5, rely = 0.8, anchor=CENTER)
def Odd():
    start()
    ls = 0
    global difficulty
    if rand%2!=0:
        global points
        label = Label(frame, text="Y̳O̳U̳ ̳G̳O̳T̳ ̳I̳T̳", fg='black', bg='#77fc03', font=(20))
        label.place(relx=0.5, rely=0.3, anchor=CENTER)
        if muted == False:
            play("E:\\MY PROGRAMS\\sounds\\Speech On.wav")
        if points >= 500:
            message("𝐅𝐫𝐚𝐦𝐞 𝐲𝐨𝐮𝐫 𝐦𝐨𝐯𝐞𝐬 𝐜𝐚𝐫𝐞𝐟𝐮𝐥𝐥𝐲")
        points += 100
    else:
        label = Label(frame, text="♥ You didn't get it ♥")
        label.place(relx=0.5, rely=0.3, anchor=CENTER)
        if muted == False:
            play("E:\\MY PROGRAMS\\sounds\\Speech Off.wav")
        if points > 500:
            message("˜”*°•.˜”*°• 𝚂𝚘 𝚌𝚕𝚘𝚜𝚎 𝚢𝚎𝚝 𝚜𝚘 𝚏𝚊𝚛 •°*”˜.•°*”˜")
        if difficulty == 2:
            if points<=0:
                points-=100
            else:
                points = 0
        elif difficulty == 0:
            points = 0
        elif difficulty == 1:
            if points>0:
                points-=100
            elif points==0:
                points = 0
        elif difficulty == 4:
            points = points
        ls = points
    label2 = Label(frame, text=f"𝙻𝚊𝚜𝚝 𝚜𝚌𝚘𝚛𝚎 : {ls}")
    label2.place(relx=0.5, rely=0.9, anchor=CENTER)
    label1 = Label(frame, text=f"ⓅⓄⒾⓃⓉⓈ    : {points}", fg='black', bg='#77fc03',font=('Central',35, 'bold'))
    label1.place(relx=0.5, rely=0.7, anchor=CENTER)
    if points >= win_score:
        pwin()
def Even():
    start()
    ls = 0
    global difficulty
    if rand%2==0:
        global points
        label = Label(frame, text="Y̳O̳U̳ ̳G̳O̳T̳ ̳I̳T̳", fg='black', bg='#77fc03', font=(20))
        label.place(relx=0.5, rely=0.3, anchor=CENTER)
        if muted == False:
            play("E:\\MY PROGRAMS\\sounds\\Speech On.wav")
        if points >= 500:
            message("𝐅𝐫𝐚𝐦𝐞 𝐲𝐨𝐮𝐫 𝐦𝐨𝐯𝐞𝐬 𝐜𝐚𝐫𝐞𝐟𝐮𝐥𝐥𝐲")
        points += 100
    else:
        label = Label(frame, text="♥ You didn't get it ♥")
        label.place(relx=0.5, rely=0.3, anchor=CENTER)
        ls = points
        if muted == False:
            play("E:\\MY PROGRAMS\\sounds\\Speech Off.wav")
        if points > 500:
            message("˜”*°•.˜”*°• 𝚂𝚘 𝚌𝚕𝚘𝚜𝚎 𝚢𝚎𝚝 𝚜𝚘 𝚏𝚊𝚛 •°*”˜.•°*”˜")
        if difficulty == 2:
            if points<=0:
                points-=100
            else:
                points = 0
        elif difficulty == 0:
            points = 0
        elif difficulty == 1:
            if points>0:
                points-=100
            elif points==0:
                points = 0
        elif difficulty == 4:
            points = points
    label2 = Label(frame, text=f"𝙻𝚊𝚜𝚝 𝚜𝚌𝚘𝚛𝚎 : {ls}")
    label2.place(relx=0.5, rely=0.9, anchor=CENTER)
    label1 = Label(frame, text=f"ⓅⓄⒾⓃⓉⓈ    : {points}", fg='black', bg='#77fc03',font=('Central',35, 'bold'))
    label1.place(relx=0.5, rely=0.7, anchor=CENTER)
    if points >= win_score:
        pwin()
def exit():
    if muted == False:
        play("E:\\MY PROGRAMS\\sounds\\Speech Misrecognition.wav")
    main_menu()
def pwin():
    for widgets in frame.winfo_children():
      widgets.destroy()
    global img2
    frk1 = Label(frame, image=img2)
    frk1.pack()
    label = Label(frame, text="𝕿𝖍𝖊 𝖔𝖉𝖉𝖘 𝖔𝖋 𝖙𝖍𝖎𝖘 𝖍𝖆𝖕𝖕𝖊𝖓𝖎𝖓𝖌 𝖆𝖗𝖊 0.0009765625% (𝓸𝓷 𝓝𝓸𝓻𝓶𝓪𝓵 𝓓𝓲𝓯𝓯𝓲𝓬𝓾𝓵𝓽𝔂)", bg='#77fc03', fg='white', font=('Central', 30, 'bold'))
    label.place(relx=0.5, rely=0.3, anchor=CENTER)
    win = Label(frame, text="▀▄▀▄▀▄ 【ＹＯＵ　ＷＯＮ】 ▄▀▄▀▄▀", fg = 'white', bg= '#03a9fc', font=('Central', 50, ' bold'))
    win.place(relx=0.5, rely= 0.5, anchor=CENTER)
    button = Button(frame, text="𝐄𝐗𝐈𝐓", bg='#ff0000', fg='white', font=('Central', 20,'bold'), command=exit)
    button.place(relx=0.5, rely=0.92, anchor=CENTER)

def run_once(f):
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            wrapper.has_run = True
            return f(*args, **kwargs)
    wrapper.has_run = False
    return wrapper

@run_once
def ding():
    play("E:\\MY PROGRAMS\\sounds\\ding.wav")

def mute():
    play("E:\\MY PROGRAMS\\sounds\\ding.wav")
    global muted 
    if muted:
        muted = False
    else :
        muted = True
def cdif2():
    play("E:\\MY PROGRAMS\\sounds\\ding.wav")
    global difficulty
    difficulty = 2
    start()
def cdif0():
    play("E:\\MY PROGRAMS\\sounds\\ding.wav")
    global difficulty
    difficulty = 0
    start()
def cdif1():
    play("E:\\MY PROGRAMS\\sounds\\ding.wav")
    global difficulty
    difficulty = 1
    start()
def cdif4():
    play("E:\\MY PROGRAMS\\sounds\\ding.wav")
    global difficulty
    difficulty = 4
    start()

def set():
    play("E:\\MY PROGRAMS\\sounds\\ding.wav")
    current_value_label = ttk.Label(
    frame,
    text='Current Value:')
    current_value_label.pack()
    current_value = tkinter.DoubleVar()
    def get_current_value():
        return '{: .2f}'.format(current_value.get())
    value_label = ttk.Label(
    frame,
    text=get_current_value())
    value_label.pack()
    def slider_changed(event):
        value_label.configure(text=get_current_value())
    
    global win_score
    for widgets in frame.winfo_children():
        widgets.destroy()
    global img3
    global difficulty
    frk = Label(frame, image=img3)
    frk.pack()
    # label = Label(frame, text="   𝕊𝕖𝕥𝕥𝕚𝕟𝕘𝕤   ", fg='black', bg='grey', font=('Central',40, 'bold'))
    # label.place(relx = 0.5, rely = 0.2, anchor=CENTER)
    muteb = Button(frame, text="𝐌𝐔𝐓𝐄 / 𝐔𝐍𝐌𝐔𝐓𝐄", fg='white', relief='raised',bg='black', font=('Central',20, 'bold'), command=mute)
    muteb.place(relx=0.5,rely=0.35,anchor=CENTER)
    dif2 = Button(frame, text="ᕼᗩᖇᗪ-ᗰOᗪE", fg='white', relief='raised',bg='red', font=('Central',20, 'bold'), command=cdif2)
    dif2.place(relx=0.5,rely=0.65,anchor=CENTER)
    dif0 = Button(frame, text="ᑎOᖇᗰᗩᒪ(ᗪEᖴᗩᑌᒪT)-ᗰOᗪE", fg='white', relief='raised',bg='yellow', font=('Central',20, 'bold'), command=cdif0)
    dif0.place(relx=0.5,rely=0.55,anchor=CENTER)
    dif1 = Button(frame, text="EᗩᔕY-ᗰOᗪE", fg='white', relief='raised',bg='green', font=('Central',20, 'bold'), command=cdif1)
    dif1.place(relx=0.5,rely=0.45,anchor=CENTER)
    dif4 = Button(frame, text="SUPER [EASY]-MODE", fg='white', relief='solid',bg='brown', font=('Central',5, 'bold'), command=cdif4)
    dif4.place(relx=0.5,rely=0.9,anchor=CENTER)
    # label1 = Label(frame, text="Set Win Score:", fg='white', bg='black', font=('Central',15, 'bold'))
    # label1.place(relx = 0.5, rely = 0.55, anchor=CENTER)
    back = Button(frame, text="Ｂａｃｋ", fg='white', relief='raised',bg='black', font=('Central',25, 'bold'), command=start)
    back.place(relx=0.5,rely=0.75,anchor=CENTER)
def start():
    global rand
    rand = randint(1,100)
    #The code line below will tell the last rand number chosen by the game
    # print(rand)
    ding()
    global points
    window.attributes('-fullscreen', True)
    global hs
    global z
    try:
        if points > hs:
            hs = points
    except:
        hs = 0
    z = 0
    for widgets in frame.winfo_children():
        widgets.destroy()
    global img4
    frk = Label(frame, image=img4)
    frk.pack()
    label = Label(frame, text="𝙶𝚞𝚎𝚜𝚜 𝚎𝚒𝚝𝚑𝚎𝚛 𝚝𝚑𝚎 𝚛𝚎𝚜𝚞𝚕𝚝 𝚒𝚜 𝙷𝙴𝙰𝙳𝚂 𝚘𝚛 𝚃𝙰𝙸𝙻𝚂", fg='White', bg='Black', font=('Central',20, 'bold'))
    label.place(relx=0.5, rely=0.09, anchor=CENTER)
    odd = Button(frame, text="H͓̽E͓̽A͓̽D͓̽S͓̽", fg='white', relief='flat',bg='#009dff', font=('Central',35, 'bold'), command=Odd)
    odd.place(relx=0.4,rely=0.5,anchor=CENTER)
    even = Button(frame, text="T͓̽A͓̽I͓̽L͓̽S͓̽", fg='white', relief='flat',bg='#ff7700', font=('Central',35, 'bold'), command=Even)
    even.place(relx=0.6,rely=0.5,anchor=CENTER)
    fs = Button(frame, text="   乂   ", relief='groove', bg='red', fg='black', font=('Central', 20,'bold'), command=exit)
    fs.place(relx=0.95, rely=0.05, anchor=CENTER)
    setb = Button(frame, text="  【...】  ", relief='ridge', bg='gray', fg='black', font=('Central', 20,'bold'), command=set)
    setb.place(relx=0.05, rely=0.05, anchor=CENTER)
    label2 = Label(frame, text=f"🅷🅸🅶🅷 🆂🅲🅾🆁🅴: {hs}", bg='yellow', fg='black', font=('Central', 30,'bold'))
    label2.place(relx=0.5, rely=0.03, anchor=CENTER)

def __init__(self):
    print(hs)

difficulty = 0
def main_menu():
    for widgets in frame.winfo_children():
        widgets.destroy()
    window.attributes('-fullscreen', True)
    global points
    points = 0
    global img
    frk = Label(frame, image=img)
    frk.pack()
    play("E:\\MY PROGRAMS\\sounds\\ding.wav")
    # label = Label(frame, text="Double or Nothing", fg='White', bg='Black', font=('Central',20, 'bold'))
    # label.place(relx=0.5, rely=0.07, anchor=CENTER)
    label = Label(frame, text="𝓗𝓮𝓵𝓵𝓸 𝓦𝓪𝓷𝓷𝓪 𝓣𝓮𝓼𝓽 𝔂𝓸𝓾𝓻 𝓵𝓾𝓬𝓴?\n 𝓘𝓷 𝓽𝓱𝓲𝓼 𝓰𝓪𝓶𝓮 𝔀𝓮 𝔀𝓲𝓵𝓵 𝓽𝓸𝓼𝓼 𝓪 𝓬𝓸𝓲𝓷 𝓪𝓷𝓭 𝔂𝓸𝓾 𝔀𝓲𝓵𝓵 𝓱𝓪𝓿𝓮 𝓽𝓸 \n 𝓖𝓾𝓮𝓼𝓼 𝓮𝓲𝓽𝓱𝓮𝓻 𝓽𝓱𝓮 𝓻𝓮𝓼𝓾𝓵𝓽 𝓲𝓼 𝓗𝓮𝓪𝓭𝓼 𝓸𝓻 𝓣𝓪𝓲𝓵𝓼\n 𝓘𝓯 𝔂𝓸𝓾 𝓰𝓮𝓽 𝓲𝓽 𝓻𝓲𝓰𝓱𝓽 𝔂𝓸𝓾𝓻 𝓹𝓸𝓲𝓷𝓽𝓼 𝔀𝓲𝓵𝓵 𝓫𝓮 𝓲𝓷𝓬𝓻𝓮𝓪𝓼𝓮𝓭 𝓫𝔂 100 𝓪𝓷𝓭 \n 𝓲𝓯 𝔂𝓸𝓾 𝓵𝓸𝓼𝓮 𝔂𝓸𝓾𝓻 𝓪𝓵𝓵 𝓹𝓸𝓲𝓷𝓽𝓼 𝔀𝓲𝓵𝓵 𝓫𝓮 𝓭𝓮𝓭𝓾𝓬𝓽𝓮𝓭", fg='black', bg='yellow', font=('Cursive',20, 'bold'))
    label.place(relx=0.5, rely=0.2, anchor=CENTER)
    bs = Button(frame, text="丂ㄒ卂尺ㄒ", fg='black', relief='flat',bg='grey', font=('Central',35, 'bold'), command=start)
    bs.place(relx=0.5, rely=0.8, anchor=CENTER)
    button = Button(frame, text="ＥＸＩＴ", bg='red', fg='white', font=('Central', 20,'bold'), command=sys.exit)
    button.place(relx=0.935, rely=0.05, anchor=CENTER)
if __name__ == "__main__":
    main_menu()
    mainloop()
