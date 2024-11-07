import tkinter as tk


def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))


def button_clear():
    entry.delete(0, tk.END)


def button_equal():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")


root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=30)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

buttons = [
    ("7", 1, 0),  # Button 7
    ("8", 1, 1),  # Button 8
    ("9", 1, 2),  # Button 9
    ("/", 1, 3),  # Divide button
    ("4", 2, 0),  # Button 4
    ("5", 2, 1),  # Button 5
    ("6", 2, 2),  # Button 6
    ("*", 2, 3),  # Multiply button
    ("1", 3, 0),  # Button 1
    ("2", 3, 1),  # Button 2
    ("3", 3, 2),  # Button 3
    ("-", 3, 3),  # Subtract button
    ("0", 4, 0),  # Button 0
    (".", 4, 1),  # Decimal point button
    ("=", 4, 2),  # Equal button
    ("+", 4, 3)   # Add button
]

for button_text, row, column in buttons:
    button = tk.Button(root, text=button_text, padx=20, pady=10, command=lambda text=button_text: button_click(text))
    button.grid(row=row, column=column, padx=5, pady=5)

clear_button = tk.Button(root, text="C", padx=20, pady=10, command=button_clear)
clear_button.grid(row=5, column=0, padx=5, pady=5)

equal_button = tk.Button(root, text="=", padx=30, pady=10, command=button_equal)
equal_button.grid(row=5, column=1, columnspan=3, padx=5, pady=5)

root.mainloop()
