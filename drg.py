import random
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox

def open_main_window(players):
    root = Tk()
    root.eval("tk::PlaceWindow . Centre")
    root.title(" All or Nothing game")
    root.iconbitmap("dice_icon_160194.ico")
    root.geometry("600x600")
    root.config(background="cyan3")
    root.maxsize(width=600,height=600)
    root.minsize(width=600,height=600)

    l0 = Label(root, text = "PLAYER 1")
    l0.config(font =("Courier", 14))
    l0.place(x=50,y=20)

    l1 = Label(root, text = "PLAYER 2")
    l1.config(font =("Courier", 14))
    l1.place(x=453,y=20)

    l2 = Label(root, text = "PLAYER 3")
    l2.config(font =("Courier", 14))
    l2.place(x=50,y=420)

    l3 = Label(root, text = "PLAYER 4")
    l3.config(font =("Courier", 14))
    l3.place(x=453,y=420)
    
    s1 = Label(root, text = "SCORE",background="cyan3")
    s1.config(font =("Courier", 14))
    s1.place(x=200,y=20)

    s2 = Label(root, text = "SCORE",background="cyan3")
    s2.config(font =("Courier", 14))
    s2.place(x=350,y=20)

    s3 = Label(root, text = "SCORE",background="cyan3")
    s3.config(font =("Courier", 14))
    s3.place(x=200,y=420)

    s4 = Label(root, text = "SCORE",background="cyan3")
    s4.config(font =("Courier", 14))
    s4.place(x=350,y=420)
     
   

    img= Image.open("among_us_player_orange_icon_156939.png")
    res_img=img.resize((100,100))
    img=ImageTk.PhotoImage(res_img)
    label1 = Label(image=img)
    label1.grid(row=0, column=0, padx=(50, 0), pady=(50, 0))

    img1= Image.open("among_us_player_red_icon_156942.png")
    res_img1=img1.resize((100,100))
    img1=ImageTk.PhotoImage(res_img1)
    label2 = Label(image=img1)
    label2.grid(row=0, column=1, padx=(300, 0), pady=( 50, 0))

    img2= Image.open("7033734_among us_icon.png")
    res_img2=img2.resize((100,100))
    img2=ImageTk.PhotoImage(res_img2)
    label3 = Label(image=img2)
    label3.grid(row=1, column=0, padx=(50, 0), pady=(300, 400))

    img3= Image.open("among_us_player_light_green_icon_156936.png")
    res_img3=img3.resize((100,100))
    img3=ImageTk.PhotoImage(res_img3)
    label4 = Label(image=img3)
    label4.grid(row=1, column=1, padx=(300, 0), pady=(300,400))

    separator1 = ttk.Separator(root,orient="vertical")
    separator1.place(relx=0.5, rely=0, relwidth=0.01, relheight=1)


    separator2 = ttk.Separator(root,orient="horizontal")
    separator2.place(relx=0., rely=0.5, relwidth=1.5, relheight=0.01)

    frame = Frame(root, bg="black")
    frame.place(relx=0.5, rely=0.48, anchor=CENTER,)

    # Add buttons on the frame
    button1 = Button(frame, text="ROLL",command= lambda: roll())
    button1.pack(side=LEFT, padx=10,pady=10)

    
    button2 = Button(frame, text="SKIP")
    button2.pack(side=RIGHT, padx=10,pady=10)

    frame1 = Frame(root, background="black")
    frame1.place(relx=0.5, rely=0.537, anchor=CENTER,)
    roll_label = Label(frame1, text="You Rolled a : ",)
    roll_label.pack()

    def roll():
        min_value = 1
        max_value = 6
        roll = random.randint(min_value, max_value)
        roll_label.config(text="You Rolled a :    " + str(roll))
        return roll
    root.mainloop()



max_score=50

def get_num_players():
    num_players = num_players_var.get()
    if num_players == 0:
        messagebox.showerror("Error!!", "Please select the number of players.")
    else:
        input_window.destroy()
        open_main_window(num_players)
                

    

# Create input window for number of players
input_window = Tk()
input_window.eval("tk::PlaceWindow . Centre")
input_window.title("Number of Players")
label = Label(input_window, text="Select the number of players:")
label.pack()

num_players_var = IntVar()

def check_player_limit():
    if sum([num_players_var.get() == i for i in range(2, 5)]) > 1:
        messagebox.showerror("Error!!", "Please select only one number of players.")
        return False
    return True

# Create Checkbuttons for each possible number of players
checkbutton_2 = Checkbutton(input_window, text="2 Players", variable=num_players_var, onvalue=2, offvalue=0)
checkbutton_2.pack()
checkbutton_3 = Checkbutton(input_window, text="3 Players", variable=num_players_var, onvalue=3, offvalue=0)
checkbutton_3.pack()
checkbutton_4 = Checkbutton(input_window, text="4 Players", variable=num_players_var, onvalue=4, offvalue=0)
checkbutton_4.pack()
button = Button(input_window, text="OK", command=get_num_players)
button.pack()

input_window.mainloop()









