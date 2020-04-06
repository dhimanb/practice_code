import tkinter as t
import functools as fc
import sys

"""
References used to solve this problem

# Youtube: Build A Simple Calculator App - Python Tkinter GUI Tutorial #5
# https://www.youtube.com/watch?v=F5PfbC5ld-Q&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=5

# stackoverflow: How to make tkinter button widget take up full width of grid
# https://stackoverflow.com/a/43189065/2773366

# stackoverflow: tkinter Entry() height
# https://stackoverflow.com/questions/24501606/tkinter-python-entry-height

# stackoverflow: Passing value to button click event
# https://stackoverflow.com/a/61055777/2773366

# https://www.tutorialspoint.com/What-is-the-most-elegant-way-to-check-if-the-string-is-empty-in-Python

"""

# global variables
# -----------------------------------------------
computed_number:float
last_operation:str


# helper function
# -----------------------------------------------
def create_button(caption:str, row:int, column:int, command, colspan=None):
    btn = t.Button(root, text=caption, width=6, padx=15, pady=15, command=command)
    if colspan == None:
        btn.grid(row=row, column=column, sticky='nesw')
    else:
        btn.grid(row=row, column=column, columnspan=colspan, sticky='nesw')
    return btn

def update_comment(data):
    comment = calc_comment.cget("text") + " " + data
    calc_comment.configure(text=comment)

def init_global():
    global computed_number, last_operation
    computed_number = 0
    last_operation = '='

# button events
# -----------------------------------------------
def allclear_click():
    init_global()
    clear_click()
    calc_comment.configure(text="")

def clear_click():
    calc_entry.delete("1.0", t.END)

def exit_click():
    sys.exit()

def number_click(number:str):
    calc_entry.insert(t.END, number)


def operator_click(op:str):
    global computed_number, last_operation

    # compute the new computed number
    str_number = calc_entry.get('1.0', t.END)
    number_has_entry = str_number.strip()
    entered_number = float(str_number) if number_has_entry else 0

    # type in what the user entered
    update_comment(str(entered_number) + "\n" + op if (number_has_entry) else op )
    
    if (last_operation == '+'):
        computed_number += entered_number
    elif (last_operation == '-'):
        computed_number -= entered_number
    elif (last_operation == '*'):
        computed_number *= entered_number
    elif (last_operation == '/'):
        computed_number /= entered_number
    elif (last_operation == '='):
        if number_has_entry:
            computed_number = entered_number

    last_operation = op

    clear_click()
    if (op == "="):
        update_comment(str(computed_number) + "\n\n")


# start of main program 
# -----------------------------------------------

init_global()

root = t.Tk()
root.title("Practice Python - A very simple calculator")

row = 0
calc_entry = t.Text(root, width=25, height=1, font=('Courier', 30))
calc_entry.grid(row=row, column=0, columnspan=5)

row += 1
create_button(caption="Exit", command =exit_click, row=row, column=0)
create_button(caption="  ", command =None, row=row, column=1)
create_button(caption="A-C", command =allclear_click, row=row, column=2)
create_button(caption="Clear", command =clear_click, row=row, column=3)

calc_comment = t.Label(root, text=" ", width=20, justify = t.RIGHT, 
                    font=('Courier', 10), anchor="ne")
calc_comment.grid(row=row, column=4, rowspan=5)

# print the numbers
row += 1
for startingNumber in (7, 4, 1):
    
    for increment in range(0, 3):
        number = startingNumber+increment
        
        create_button(caption=number, row=row, column=increment,
                command=fc.partial(number_click, number))

    row += 1

create_button(caption="0", command=lambda: number_click(0), row=row, column=0)

# print the special operations
create_button(caption=".", command=lambda: number_click('.'), row=row, column=1)
create_button(caption="=", command=lambda: operator_click('='), row=row, column=2)

# print the operators
row = 2
for op in ('/', '*', '-', '+'):
    create_button(caption=op, row=row, column=3,  
                        command=fc.partial(operator_click, op))
    row += 1
    
root.mainloop()