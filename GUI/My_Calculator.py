# Import Required Libraries
from tkinter import*
from PIL import Image

# Creating Parent Root
root = Tk()
root.title("Calculator")
root.iconbitmap('d:/Geri/Arts/Computer Science/Python/Python Projects/GUI/calculator.ico')
root.geometry("317x355")

# Creating Entry Tab
e = Entry(root, width=16, borderwidth=5, bg="Black", fg="White", font=('Helvetica', 25))
e.place(x=8, y=10)

# Defining the Buttons
def button_click(number):
	current = e.get()
	e.delete(0, END)
	e.insert(0, str(current) + str(number))

def button_clear():
	e.delete(0, END)

def button_add():
	first_number = e.get()
	global f_num
	global math
	math = "addition"
	f_num = int(first_number)
	e.delete(0, END)

def button_equal():
	second_number = e.get()
	e.delete(0, END)

	if math == "addition":
		e.insert(0, f_num + int(second_number))

	if math == "subtraction":
		e.insert(0, f_num - int(second_number))

	if math == "multiplication":
		e.insert(0, f_num * int(second_number))

	if math == "division":
		e.insert(0, f_num / int(second_number))

def	button_subtract():
	first_number = e.get()
	global f_num
	global math
	math = "subtraction"
	f_num = int(first_number)
	e.delete(0, END)

def	button_multiply():
	first_number = e.get()
	global f_num
	global math
	math = "multiplication"
	f_num = int(first_number)
	e.delete(0, END)

def	button_divide():
	first_number = e.get()
	global f_num
	global math
	math = "division"
	f_num = int(first_number)
	e.delete(0, END)

# Displaying the Buttons
button_1 = Button(root, padx=20, pady=5, borderwidth=3, bg="Blue", fg="White", text="1", font=1, command=lambda: button_click(1))
button_2 = Button(root, padx=20, pady=5, borderwidth=3, bg="Blue", fg="White", text="2", font=1, command=lambda: button_click(2))
button_3 = Button(root, padx=20, pady=5, borderwidth=3, bg="Blue", fg="White", text="3", font=1, command=lambda: button_click(3))
button_4 = Button(root, padx=20, pady=5, borderwidth=3, bg="Blue", fg="White", text="4", font=1, command=lambda: button_click(4))
button_5 = Button(root, padx=20, pady=5, borderwidth=3, bg="Blue", fg="White", text="5", font=1, command=lambda: button_click(5))
button_6 = Button(root, padx=20, pady=5, borderwidth=3, bg="Blue", fg="White", text="6", font=1, command=lambda: button_click(6))
button_7 = Button(root, padx=20, pady=5, borderwidth=3, bg="Blue", fg="White", text="7", font=1, command=lambda: button_click(7))
button_8 = Button(root, padx=20, pady=5, borderwidth=3, bg="Blue", fg="White", text="8", font=1, command=lambda: button_click(8))
button_9 = Button(root, padx=20, pady=5, borderwidth=3, bg="Blue", fg="White", text="9", font=1, command=lambda: button_click(9))
button_0 = Button(root, padx=20, pady=5, borderwidth=3, bg="Blue", fg="White", text="0", font=1, command=lambda: button_click(0))
button_equal = Button(root, padx=57, pady=5, borderwidth=3, bg="Green", fg="White", text="=", font=1, command=button_equal)
button_add = Button(root, padx=20, pady=5, borderwidth=3, bg="Orange", fg="Black", text="+", font=1, command=button_add)
button_subtract = Button(root, padx=22, pady=5, borderwidth=3, bg="Orange", fg="Black", text="-", font=1, command=button_subtract)
button_clear = Button(root, padx=50, pady=5, borderwidth=3, bg="Red", fg="White", text="CE", font=1, command=button_clear)
button_multiply = Button(root, padx=22, pady=5, borderwidth=3, bg="Orange", fg="Black", text="*", font=1, command=button_multiply)
button_divide = Button(root, padx=22, pady=5, borderwidth=3, bg="Orange", fg="Black", text="/", font=1, command=button_divide)

# Positioning the Buttons
button_1.place(x=10, y=70)
button_2.place(x=86, y=70)
button_3.place(x=162, y=70)
button_4.place(x=237, y=70)

button_5.place(x=10, y=127)
button_6.place(x=86, y=127)
button_7.place(x=162, y=127)
button_8.place(x=237, y=127)

button_9.place(x=10, y=184)
button_0.place(x=86, y=184)
button_equal.place(x=162, y=184)

button_add.place(x=10, y=241)
button_subtract.place(x=86, y=241)
button_clear.place(x=162, y=241)

button_multiply.place(x=10, y=298)
button_divide.place(x=86, y=298)

root.mainloop()