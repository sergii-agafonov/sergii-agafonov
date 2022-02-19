import tkinter as tk
import random

window = tk.Tk()
window.geometry("700x350")

# result = 0


# random for dice throwing
def dice_throw():
    beg_range = int(float(entry_my.get()))
    end_range = int(float(entry_my2.get()))
    # global result
    result = random.randint(beg_range, end_range)
    label.config(text=result)


# label1
greeting = tk.Label(text='Place the number of sides for you dice',
                    bg="#C8A554",
                    # width=20,
                    # height=20
                    )
greeting.pack()
# input from user
entry_my = tk.Entry(text='Begin of range', fg='blue', width=20)
entry_my.pack()

entry_my2 = tk.Entry(text='End of range', fg='blue', width=20)
entry_my2.pack()

# button
button_roll = tk.Button(text='Roll the dice, my Dear gamer',
                        foreground="black",  # Устанавливает белый текст
                        background="deep sky blue",  # Устанавливает фон
                        width=25,
                        height=5,
                        command=dice_throw
                        )
button_roll.pack()

# Label2 output from user
label = tk.Label(bg="#BBE8EF", width=20, font=("Arial", 25))
label.pack()


tk.mainloop()
