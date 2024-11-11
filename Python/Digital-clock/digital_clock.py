from tkinter import Tk, Label
from time import strftime

def clock():
    current_time = strftime('%H:%M:%S')
    lb_hour.config(text=current_time)
    lb_hour.after(1000, clock)

window = Tk()
window.title('Clock')
window.configure(bg='black')

lb_hour = Label(window, text='12', font=('calibri', 40, 'bold'), bg='black', fg='white')
lb_hour.pack()

clock()
window.mainloop()