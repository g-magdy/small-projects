import tkinter

window = tkinter.Tk()
window.geometry("1050x800")
window.title("S C O R E B O A R D")
window.resizable(width=True, height=True)
window.config(padx=110, pady=200)
FONT = ("Calibri", 40, "bold")
FONT_BUTTON = ("calibri", 30)

# background
img = tkinter.PhotoImage(file="scoreboard.png")
canvas = tkinter.Canvas(window, width=1050, height=800)
canvas.create_image(525, 400, image=img)
canvas.place(x=-100, y=-180)

up_img = tkinter.PhotoImage(file="up-arrow-sq.png")
down_img = tkinter.PhotoImage(file="down-arrow-sq.png")

# team 1 label
team1_label = tkinter.Entry(font=FONT, justify="center", bg="#cdcfce", borderwidth=0)
team1_label.config(width=15)
team1_label.grid(row=0, column=0, padx=5, pady=15)

# team 2 label
team2_label = tkinter.Entry(font=FONT, justify="center", bg="#cdcfce", borderwidth=0)
team2_label.config(width=15)
team2_label.grid(row=0, column=1, padx=17, pady=15)

# team 1 upvote
team1_up = tkinter.Button(image=up_img, highlightthickness=0,
                          command=lambda: team1_score.config(text=f"{int(team1_score.cget('text'))+1}")
                          )
team1_up.grid(row=1, column=0, pady=10)

# team 2 upvote
team2_up = tkinter.Button(image=up_img, highlightthickness=0,
                          command=lambda: team2_score.config(text=f"{int(team2_score.cget('text'))+1}")
                          )
team2_up.grid(row=1, column=1, pady=10)

# team 1 score
team1_score = tkinter.Label(text=0, font=("calibri", 85, "normal"), padx=20, pady=20, bg="#cdcfce")
team1_score.grid(row=2,column=0, pady=5)

# team 2 score
team2_score = tkinter.Label(text=0, font=("calibri", 85, "normal"), padx=20, pady=20, bg="#cdcfce")
team2_score.grid(row=2,column=1, pady=5)

# team 1 downvote
team1_down = tkinter.Button(image=down_img, highlightthickness=0,
                            command=lambda: team1_score.config(text=f"{int(team1_score.cget('text'))-1}")
                            )
team1_down.grid(row=3, column=0, pady=10)
# team 2 downvote
team2_down = tkinter.Button(image=down_img, highlightthickness=0,
                            command=lambda: team2_score.config(text=f"{int(team2_score.cget('text'))-1}")
                            )
team2_down.grid(row=3, column=1, pady=10)


window.mainloop()