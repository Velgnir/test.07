from tkinter import *

canvas_width = 700
canvas_height = 700
brush_size = 10
color = "#fff700"

def convert_base(num, to_base=10, from_base=10):
    # first convert to decimal number
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    # now convert decimal to 'to_base' base
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]


def main(event):
	x1=event.x
	y1=event.y
	i = 1
	while i<985:
		i=i+1
		z=i
		while z>1:
			color=convert_base((str(int(convert_base("fff700",to_base=10,from_base=16))-z*16970)),to_base=16,from_base=10)
			if (int(convert_base(color, to_base=10, from_base=16))<=1048575) and (color[0]!="0"):
				color = "0"+color
			if (int(convert_base(color, to_base=10, from_base=16))<=65535) and (color[1]!="0"):
				color = "0"+color
			if (int(convert_base(color, to_base=10, from_base=16))<=4095) and (color[2]!="0"):
				color = "0"+color
			if (int(convert_base(color, to_base=10, from_base=16))<=255) and (color[3]!="0"):
				color = "0"+color
			if (int(convert_base(color, to_base=10, from_base=16))<=15) and (color[4]!="0"):
				color = "0"+color
			w.create_oval(x1-z,y1-z,x1+z,y1+z,fill="#"+color, outline="#"+color)
			z-=z
		root.update()


root = Tk()
root.title("Test.07")

w = Canvas(root,
	width=canvas_width,
	height=canvas_height,
	bg="white")

w.bind("<B1-Motion>",main)

w.grid(row=2, column=0,
	columnspan=7, padx=5,
	pady=5, sticky = E+W+S+N)

w.columnconfigure(6, weight=1)
w.rowconfigure(2, weight=1)


root.mainloop()