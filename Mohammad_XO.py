import subprocess
subprocess.call("cls", shell=True)
from tkinter import *  
from tkinter import messagebox
from tkinter import ttk
from random import *  

state = ["X", "O"]

turn = "X"          
board = ["", "", "", "", "", "", "", "", ""]
game_over = False


def XO_Game():
    global turn, board, game_over

    def click(index, btn):
        global turn, game_over

        if game_over:
            return

        if turn != "X":
            return  

        if board[index] != "":
            return

        place_mark(index, btn, "X")

        if game_over:
            return

        turn = "O"
        l1.config(text="Turn : Machine")
        p1.after(400, machine_move)

    def machine_move():
        global turn, game_over

        if game_over:
            return

        empty_cells = [i for i in range(9) if board[i] == ""]
        if not empty_cells:
            return

        index = choice(empty_cells)
        place_mark(index, buttons[index], "O")

        if game_over:
            return

        turn = "X"
        l1.config(text="Turn : Human")

    def place_mark(index, btn, player):
        global game_over

        board[index] = player
        btn.config(text=player)

        if check_winner(player):
            winner_name = "Human" if player == "X" else "Machine"
            messagebox.showinfo("Winner", winner_name + " Has Been Wined")
            game_over = True
            return

        if "" not in board:
            messagebox.showinfo("Draw", "No One Wined")
            game_over = True
            return

    def check_winner(player):
        win_states = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6),
        ]
        for a, b, c in win_states:
            if board[a] == player and board[b] == player and board[c] == player:
                return True
        return False

    def restart():
        global board, turn, game_over
        board = ["", "", "", "", "", "", "", "", ""]
        turn = "X"
        game_over = False
        l1.config(text="Turn : X")
        for b in buttons:
            b.config(text="")

    p1 = Tk()
    p1.title("X O Game - vs Machine")
    p1.resizable(False, False)
    p1.config(bg="#01a2ad")
    p1.geometry("400x450")

    l1 = Label(p1, text="Turn : X", font=("Arial", 14), bg="#01a2ad", fg="white")
    l1.place(x=140, y=40)

    b1 = Button(p1, font=("Arial", 16))
    b1.place(x=100, y=100, width=50, height=50)

    b2 = Button(p1, font=("Arial", 16))
    b2.place(x=100, y=160, width=50, height=50)

    b3 = Button(p1, font=("Arial", 16))
    b3.place(x=100, y=220, width=50, height=50)

    b4 = Button(p1, font=("Arial", 16))
    b4.place(x=160, y=100, width=50, height=50)

    b5 = Button(p1, font=("Arial", 16))
    b5.place(x=160, y=160, width=50, height=50)

    b6 = Button(p1, font=("Arial", 16))
    b6.place(x=160, y=220, width=50, height=50)

    b7 = Button(p1, font=("Arial", 16))
    b7.place(x=220, y=100, width=50, height=50)

    b8 = Button(p1, font=("Arial", 16))
    b8.place(x=220, y=160, width=50, height=50)

    b9 = Button(p1, font=("Arial", 16))
    b9.place(x=220, y=220, width=50, height=50)


    buttons = [b1, b4, b7, b2, b5, b8, b3, b6, b9]

    for i, b in enumerate(buttons):
        b.config(command=lambda i=i, b=b: click(i, b))

    b_restart = Button(p1, text="Restart", width=17, command=restart)
    b_restart.place(x=120, y=380)

    p1.mainloop()


XO_Game()