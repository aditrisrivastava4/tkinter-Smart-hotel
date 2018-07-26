from tkinter import *

sh = Tk()
sh.title("Smart Hotel")

buttons = [ 'fan','ac','tv']
row = 0
col = 1
for i in buttons:
    button_style = 'raised'
    action = lambda x = i: click_event(x)
    Radiobutton(sh, text = i, command = action, height = 2) \
		.grid(row = row, column = col, sticky = 'nesw')
    row += 1
    if row > 2:
        row = 0
        col += 1

def click_event(key):
	window=Toplevel(sh)
	if key == 'fan':
		f=Button(window,text='on')
		f.pack(side=LEFT)
		f=Button(window,text='off')
		f.pack(side=LEFT)
		
	elif key == 'ac':
		f=Button(window,text='on')
		f.pack(side=LEFT)
		f=Button(window,text='off')
		f.pack(side=LEFT)
		f=Button(window,text='temp',command=range)
		f.pack(side=LEFT)
	elif key == 'tv':
		f=Button(window,text='on')
		f.pack(side=LEFT)
		f=Button(window,text='off')
		f.pack(side=LEFT)

def range():
	window = Toplevel(sh)
	label=Label(window,text='Select the desired temperature')
	label.pack()
	temp=Spinbox(window, from_=16, to=28)
	temp.pack()
sh.mainloop()