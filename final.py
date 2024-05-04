import random
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox

p1 = None
p2 = None
p3 = None
p4 = None
player_scores = []
player_idx = 0
curr_scr = 0
winning_mark = 20
def open_main_window(num_players):
    global p1, p2, p3, p4,player_scores, player_idx, curr_scr

    root = Tk()
    root.eval("tk::PlaceWindow . Centre")
    root.title(" All or Nothing game")
    root.iconbitmap("dice_icon_160194.ico")
    root.geometry("600x600")
    root.config(background="cyan3")
    root.maxsize(width=600, height=600)
    root.minsize(width=600, height=600)

    l0 = Label(root, text="PLAYER 1")
    l0.config(font=("Courier", 14))
    l0.place(x=20, y=20)

    l1 = Label(root, text="PLAYER 2")
    l1.config(font=("Courier", 14))
    l1.place(x=483, y=20)

    l2 = Label(root, text="PLAYER 3")
    l2.config(font=("Courier", 14))
    l2.place(x=20, y=430)

    l3 = Label(root, text="PLAYER 4")
    l3.config(font=("Courier", 14))
    l3.place(x=483, y=430)

    s1 = Label(root, text="", background="cyan3")
    s1.config(font=("Courier", 14))
    s1.place(x=0, y=0)

    s2 = Label(root, text="", background="cyan3")
    s2.config(font=("Courier", 14))
    s2.place(x=320, y=20)

    s3 = Label(root, text="", background="cyan3")
    s3.config(font=("Courier", 14))
    s3.place(x=160, y=430)

    s4 = Label(root, text="", background="cyan3")
    s4.config(font=("Courier", 14))
    s4.place(x=320, y=430)

    img = Image.open("among_us_player_1_icon_156939.png")
    res_img = img.resize((100, 100))
    img = ImageTk.PhotoImage(res_img)
    label1 = Label(image=img,bg="cyan3")
    label1.place(x=10,y=50)

    img1 = Image.open("among_us_player_2_icon_156939.png")
    res_img1 = img1.resize((100, 100))
    img1 = ImageTk.PhotoImage(res_img1)
    label2 = Label(image=img1,bg="cyan3")
    label2.place(x=473,y=50)

    img2 = Image.open("among_us_player_3_icon_156939.png")
    res_img2 = img2.resize((100, 100))
    img2 = ImageTk.PhotoImage(res_img2)
    label3 = Label(image=img2,bg="cyan3")
    label3.place(x=20,y=460)

    img3 = Image.open("among_us_player_4_icon_156939.png")
    res_img3 = img3.resize((100, 100))
    img3 = ImageTk.PhotoImage(res_img3)
    label4 = Label(image=img3,bg="cyan3")
    label4.place(x=483,y=460)

    separator1 = ttk.Separator(root, orient="vertical")
    separator1.place(relx=0.5, rely=0, relwidth=0.01, relheight=1)

    separator2 = ttk.Separator(root, orient="horizontal")
    separator2.place(relx=0., rely=0.5, relwidth=1.5, relheight=0.01)

    frame = Frame(root, bg="black")
    frame.place(relx=0.5, rely=0.48, anchor=CENTER)

    frame1 = Frame(root, background="black")
    frame1.place(relx=0.5, rely=0.537, anchor=CENTER)
    roll_label = Label(frame1, text="You Rolled a : ")
    roll_label.pack()

    score_label = Label(frame1, text="Your score is : ")
    score_label.pack()

    ss1 = Label(root, text="TOTAL SCORE", background="cyan3")
    ss1.config(font=("Courier", 14))
    ss1.place(x=160, y=20)

    ss2 = Label(root, text="TOTAL SCORE", background="cyan3")
    ss2.config(font=("Courier", 14))
    ss2.place(x=320, y=20)

    ss3 = Label(root, text="TOTAL SCORE", background="cyan3")
    ss3.config(font=("Courier", 14))
    ss3.place(x=160, y=430)

    ss4 = Label(root, text="TOTAL SCORE", background="cyan3")
    ss4.config(font=("Courier", 14))
    ss4.place(x=320, y=430)

    
    player_scores = [0 for _ in range(num_players)]
    player_idx = 0
    curr_scr = 0  # Current score for the current player

    def check_winner():
        global player_scores
        for idx, score in enumerate(player_scores):
            if score >= winning_mark:
                messagebox.showinfo("Game Over", f"Player {idx+1} wins with a score of {score}!")
                root.quit()

    def roll():
        global curr_scr
        min_value = 1
        max_value = 6
        roll = random.randint(min_value, max_value)
        roll_label.config(text="You Rolled a :    " + str(roll))
        if roll == 1:
            messagebox.showinfo("SED", "You rolled a 1")
            player_scores[player_idx]=0
            curr_scr=0
            skip()  # Automatically skip to the next player
        else:
            check_winner()
            curr_scr += roll  # Add roll to the current score
            score_label.config(text="Your current score is : " + str(curr_scr))
            
        return roll

    def skip():
        check_winner()
        global player_idx, player_scores, curr_scr
        player_scores[player_idx] += curr_scr
        player_idx = (player_idx + 1) % num_players
        curr_scr = 0
        update_turn(player_idx)
        roll_label.config(text="You Rolled a : ")
        score_label.config(text="Your Current score is : " + str(curr_scr))
        update_total_scores()
        

    def update_turn(player_idx):
        # Clear existing turn messages
        p1.config(text="",background="cyan3",font=(25))
        p2.config(text="",background="cyan3",font=(25))
        p3.config(text="",background="cyan3",font=(25))
        p4.config(text="",background="cyan3",font=(25))

        # Display message for the next player's turn
        if player_idx == 0:
            p1.config(text="Player 1 turn has started")
        elif player_idx == 1:
            p2.config(text="Player 2 turn has started")
        elif player_idx == 2:
            p3.config(text="Player 3 turn has started")
        else:
            p4.config(text="Player 4 turn has started")
            
    def update_total_scores():
        s1.config(text=str(player_scores[0]), font=("courier",40))
        s1.place(x=205,y=70)
        
        s2.config(text=str(player_scores[1]),font=("courier",40) )
        s2.place(x=365,y=70)
        s3.config(text=str(player_scores[2]),font=("courier",40))
        s3.place(x=205,y=470)
        
        s4.config(text=str(player_scores[3]),font=("courier",40))
        s4.place(x=365,y=470)

    button1 = Button(frame, text="ROLL", command=lambda: roll())
    button1.pack(side=LEFT, padx=10, pady=10)

    button2 = Button(frame, text="SKIP", command=skip)
    button2.pack(side=RIGHT, padx=10, pady=10)

    p1 = Label(root, text="Player 1 turn has started")
    p1.config(font=("Courier", 10))
    p1.place(x=50, y=170)

    p2 = Label(root, text="PLAYER 2 turn has started")
    p2.config(font=("Courier", 10))
    p2.place(x=355, y=170)

    p3 = Label(root, text="PLAYER 3 turn has started")
    p3.config(font=("Courier", 10))
    p3.place(x=50, y=370)

    p4 = Label(root, text="PLAYER 4 turn has started")
    p4.config(font=("Courier", 10))
    p4.place(x=355, y=370)

    update_turn(player_idx)

    root.mainloop()

max_score = 50

def get_num_players():
    global player_scores
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
def open_new_game_window(winning_player):
    new_game_window = Toplevel()
    new_game_window.title("New Game or Quit")
    new_game_window.geometry("300x100")

    def start_new_game():
        new_game_window.destroy()
        # Call the function to start a new game
        # Replace this with your function to start a new game

    def quit_game():
        new_game_window.destroy()
        # Quit the application
        # Replace this with whatever code you use to quit the application

    winner_label = Label(new_game_window, text=f"Player {winning_player} wins!", font=("Courier", 14))
    winner_label.pack()

    new_game_button = Button(new_game_window, text="New Game", command=start_new_game)
    new_game_button.pack(side="left", padx=10)

    quit_button = Button(new_game_window, text="Quit", command=quit_game)
    quit_button.pack(side="right", padx=10)
    
input_window.mainloop()
