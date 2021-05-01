from tkinter import *
from data import data
from random import randint
import time

passage = data[randint(1, len(data))]
count = 0
start = 0
seconds = 0
minutes = 0
end = False


def timer():
    global canvas_timer, start, seconds, minutes, end
    if not end:
        step = time.time()
        clock = round(step - start)
        if clock > 59 and clock % 60 == 0:
            minutes += 1
        seconds = clock % 60
        canvas_timer.delete("all")
        canvas_timer.create_text(25, 25, fill="darkblue", font="Times 15 italic bold",
                                 text=f'{minutes}:{seconds}')
        canvas_timer.after(1000, timer)


def start_time():
    global start
    start = time.time()
    timer()


def calculate():
    global text_user, passage, count, canvas_accuracy, canvas_speed, window, start, end
    end = True
    stop = time.time()
    user_input = text_user.get("1.0", 'end-1c')
    passage = passage.split()
    if len(user_input) == 0:
        accuracy = 0
        speed = 0
    else:
        user_input = user_input.split()
        for i in range(0, len(passage) - 1):
            try:
                if passage[i] == user_input[i]:
                    count += 1
            except IndexError:
                break
        accuracy = count / len(user_input) * 100
        gross_speed = (60 / (stop - start)) * len(user_input)
        speed = accuracy / 100 * gross_speed
    canvas_accuracy.create_text(50, 25, fill="darkblue", font="Times 15 italic bold", text=f'{round(accuracy)}%')
    canvas_speed.create_text(50, 25, fill="darkblue", font="Times 15 italic bold", text=f'{round(speed)} wpm')


# Main Program
window = Tk()
window.title('Typing Speed Test')
window.minsize(width=1000, height=500)
window.config(padx=50, pady=10, bg='#42f5c8')


label_passage = Label(text=passage, wraplength=980, justify='center', font="Arial 15")
label_passage.grid(row=0, column=0, columnspan=2, pady=10)
button_start = Button(text="Start", command=start_time)
button_start.grid(row=1, column=0, pady=10)
canvas_timer = Canvas(window, width=50, height=50)
canvas_timer.grid(row=1, column=1)
text_user = Text(window, height=10, width=120)
text_user.grid(row=2, column=0, columnspan=2, pady=10)
button_submit = Button(text="Submit", command=calculate)
button_submit.grid(row=3, column=0, columnspan=2, pady=10)
canvas_accuracy = Canvas(window, width=100, height=50)
canvas_accuracy.grid(row=4, column=0, pady=10)
label_accuracy = Label(text='Accuracy')
label_accuracy.grid(row=5, column=0)
canvas_speed = Canvas(window, width=100, height=50)
canvas_speed.grid(row=4, column=1)
label_speed = Label(text='Speed')
label_speed.grid(row=5, column=1)

window.mainloop()
