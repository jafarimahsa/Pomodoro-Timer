from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0 
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text , text="00:00")
    check_marks.config(text='')
    label.config(text='Timer' , fg = GREEN)
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    #count_down(1 * 60)
    global reps
    reps+=1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0 :
        count_down(long_break_sec)
        label.config(text='Break' , fg = RED)
    elif reps % 2 == 0 :
        count_down(short_break_sec)
        label.config(text='Break' , fg = PINK)
    else :
        count_down(work_sec)
        label.config(text='Work' , fg = GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10 :
        count_sec = f'0{count_sec}'
    
    canvas.itemconfig(timer_text , text=f"{count_min}:{count_sec}")
    if count > 0 :
        timer = window.after(1000 , count_down , count-1)

    else :
        start_timer()
        marks =""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100 , pady=50 , bg=YELLOW)
canvas = Canvas(width=200 , height=224 , bg=YELLOW)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(102 , 112 ,image=tomato_img)
timer_text = canvas.create_text(100 , 135 , text='00:00' , fill='white' , font=(FONT_NAME , 35 , 'bold'))
#canvas.create_text(100 , 280 , text = '✔' , fill = GREEN , font=(FONT_NAME , 25 , 'bold'))
#label_frame = LabelFrame(canvas , text="Timer")
label = Label(text='Timer' , fg = GREEN , font=(FONT_NAME , 45 , 'bold') , bg = YELLOW)
check_marks = Label(text = '' , fg = GREEN , bg = YELLOW)
b1 = Button(window , text= 'Start' , command = start_timer)
b2 = Button(window , text= 'Reset' , command = reset_timer)
b1.grid(row = 2, column = 0)
b2.grid(row = 2, column = 2)
canvas.grid(row=1 , column= 1)
#count_down(1000)
label.grid(row = 0 , column = 1)
check_marks.grid(row = 3 , column = 1)
#canvas.pack()

window.mainloop()