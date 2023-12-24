import tkinter as tk


'''window = tk.Tk()
window.title("C2121")
window.geometry("600x400+400+200")
#window.resizable(True, False)
window.minsize(400, 400)
window.iconbitmap("pics/bomb.ico")

label = tk.Label(window, text="Hello Python!",
                 font=("Jokerman", 24, "bold"),
                 fg="Teal",
                 bg="yellow",
                 width=20,
                 height=2)
label.pack()


button = tk.Button(text="Click My", font=("Jokerman", 16))
button.pack()'''


timer = 100
score = 0
press_enter = True

window = tk.Tk()
window.title("Bomber")
window.geometry("600x600+450+100")
window.resizable(False, False)
window.iconbitmap("pics/bomb.ico")

label = tk.Label(text="Для початку гри натисніть [ENTER]",
                 font=("Comic Sans MS", 12, "bold"))
label.pack()

time_count = tk.Label(text=f"Залишок часу {timer}", font=("Comic Sans MS", 16, "bold"))
time_count.pack()

score_label = tk.Label(text=f"Набрані бали {score}", font=("Comic Sans MS", 16, "bold"))
score_label.pack()

img1 = tk.PhotoImage(file="pics/1.gif")
img2 = tk.PhotoImage(file="pics/2.gif")
img3 = tk.PhotoImage(file="pics/3.gif")
img4 = tk.PhotoImage(file="pics/4.gif")

bomb_label = tk.Label(image=img1)
bomb_label.pack()


def is_alive():
    global timer
    if timer <= 0:
        timer = 0
        label.config(text="Бабах! Бабах! Бабах!", fg="red")
        return False
    else:
        return True


def update_screen():
    global timer
    global score
    if timer >= 80:
        bomb_label.config(image=img1)
    elif 50 <= timer < 80:
        bomb_label.config(image=img2)
    elif 0 < timer < 50:
        bomb_label.config(image=img3)
    else:
        bomb_label.config(image=img4)

    time_count.config(text=f"Залишок часу {timer}")
    score_label.config(text=f"Набрані бали {score}")
    bomb_label.after(100, update_screen)


def update_time():
    global timer
    timer -= 5
    if is_alive():
        bomb_label.after(500, update_time)


def update_score():
    global score
    score += 1
    if is_alive():
        score_label.after(1000, update_score)


def click():
    global timer
    if is_alive():
        timer += 1


def start(event):
    global press_enter
    if not press_enter:
        pass
    else:
        update_screen()
        update_time()
        update_score()
        press_enter = False
        label.config(text="")


click_button = tk.Button(text="Тикай сюди!", font=("Comic Sans MS", 16, "bold"),
                         bg="black", fg="white", command=click)
click_button.pack()


window.bind("<Return>", start)

window.mainloop()