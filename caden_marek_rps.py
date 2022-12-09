from tkinter import *
import random


# The code is from https://www.geeksforgeeks.org/rock-paper-and-scissor-game-using-tkinter/
window = Tk()
window.geometry("300x400")
window.resizable(False, False)
window.title("RPS")
window.configure(bg='black')
computer_value = {"0": "Rock", "1": "Paper", "2": "Scissor"}


def clear_game():
    b1["state"] = "active"
    b2["state"] = "active"
    b3["state"] = "active"
    l1.config(text="Player              ")
    l3.config(text="Computer")
    l4.config(text="")


def button_disable():
    b1["state"] = "disable"
    b2["state"] = "disable"
    b3["state"] = "disable"


def rock():
    com_value = computer_value[str(random.randint(0, 2))]
    if com_value == "Rock":
        match_result = "Match Draw"
        # counters to keep track of points
        p2 = ++ 1
        l9.configure(text=p2)
    elif com_value == "Scissor":
        match_result = "Player Win"
        # counters to keep track of points
        p1 = ++ 1
        l8.configure(text=p1)
    else:
        match_result = "Computer Win"
        # counters to keep track of points
        p3 = ++ 1
        l10.configure(text=p3)
    l4.config(text=match_result)
    l1.config(text="Rock            ")
    l3.config(text=com_value)
    button_disable()


def paper():
    com_value = computer_value[str(random.randint(0, 2))]
    if com_value == "Paper":
        match_result = "Match Draw"
        # counters to keep track of points
        p2 = ++ 1
        l9.configure(text=p2)
    elif com_value == "Scissor":
        match_result = "Computer Win"
        # counters to keep track of points
        p3 = ++ 1
        l10.configure(text=p3)
    else:
        match_result = "Player Win"
        # counters to keep track of points
        p1 = ++ 1
        l8.configure(text=p1)
    l4.config(text=match_result)
    l1.config(text="Paper           ")
    l3.config(text=com_value)
    button_disable()


def scissor():
    com_value = computer_value[str(random.randint(0, 2))]
    if com_value == "Rock":
        match_result = "Computer Win"
        # counters to keep track of points
        p3 = ++ 1
        l10.configure(text=p3)
    elif com_value == "Scissor":
        match_result = "Match Draw"
        # counters to keep track of points
        p2 = ++ 1
        l9.configure(text=p2)
    else:
        match_result = "Player Win"
        # counters to keep track of points
        p1 = ++ 1
        l8.configure(text=p1)
    l4.config(text=match_result)
    l1.config(text="Scissor         ")
    l3.config(text=com_value)
    button_disable()


# New Code that Clears the scoreboard when button is clicked
def clear_score():
    l8.configure(text=0)
    l9.configure(text=0)
    l10.configure(text=0)


Label(window, text="Rock Paper Scissor", font="normal 22 bold", fg="red", bg="black").pack(pady=20)
frame = Frame(window)
frame.pack()

l1 = Label(frame, text="Player              ", font=10, fg="white", bg="black")
l2 = Label(frame, text="VS             ", font=10, fg="white", bg="black")
l3 = Label(frame, text="Computer", font=10, fg="white", bg="black")
l1.pack(side=LEFT)
l2.pack(side=LEFT)
l3.pack()
l4 = Label(window, text="", font="normal 20 bold", bg="white", width=15, borderwidth=2, relief="solid")
l4.pack(pady=20)

frame1 = Frame(window)
frame1.configure(bg="black")
frame1.pack()
b1 = Button(frame1, text="Rock", font=10, width=7, command=rock)
b2 = Button(frame1, text="Paper ", font=10, width=7, command=paper)
b3 = Button(frame1, text="Scissor", font=10, width=7, command=scissor)
b1.pack(side=LEFT, padx=10)
b2.pack(side=LEFT, padx=10)
b3.pack(padx=10)

Button(window, text="Clear Game", font=10, fg="red", bg="white", command=clear_game).pack(pady=20)

# New Code Adds a new frame for a score board
frame2 = Frame(window)
frame2.configure(bg="black")
frame2.pack()
frame3 = Frame(window)
frame3.configure(bg="black")
frame3.pack()

# Labels for the Scoreboard that has the player,draw, and computer
l5 = Label(frame2, text='Player = ', font=10, fg="white", bg="black")
l8 = Label(frame2, text=0, font=10, fg="white", bg="black")
l6 = Label(frame2, text='Draws = ', font=10, fg="white", bg="black")
l9 = Label(frame2, text=0, font=10, fg="white", bg="black")
l7 = Label(frame2, text='Computer = ', font=10, fg="white", bg="black")
l10 = Label(frame2, text=0, font=10, fg="white", bg="black")
l5.pack(side='left')
l8.pack(side='left')
l6.pack(side='left')
l9.pack(side='left')
l7.pack(side='left')
l10.pack(side='left')

# button that when clicked will reset the scoreboard
b4 = Button(frame3, text='Clear Scoreboard', font=10, fg="red", bg="white", command=clear_score)
b4.pack(pady=20, side='top')

window.mainloop()
