import os
from Tkinter import *
from tkFileDialog import askopenfilename
from PIL import Image ,ImageTk
import os
import io
if __name__ == "__main__":
    root = Tk()

    #setting up a tkinter canvas with scrollbars
    frame = Frame(root, bd=2, relief=SUNKEN)
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)
    xscroll = Scrollbar(frame, orient=HORIZONTAL)
    xscroll.grid(row=1, column=0, sticky=E+W)
    yscroll = Scrollbar(frame)
    yscroll.grid(row=0, column=1, sticky=N+S)
    canvas = Canvas(frame, bd=0, xscrollcommand=xscroll.set, yscrollcommand=yscroll.set,width=640, height=1136)
    canvas.grid(row=0, column=0, sticky=N+S+E+W)
    xscroll.config(command=canvas.xview)
    yscroll.config(command=canvas.yview)
    frame.pack(fill=BOTH,expand=1)

    #adding the image
    File = askopenfilename(parent=root, initialdir="C:/",title='Choose an image.')
    img =  Image.open(File)
    photo = ImageTk.PhotoImage(img)
    canvas.create_image(0,0,image=photo,anchor="nw")
    canvas.config(scrollregion=canvas.bbox(ALL))

    #function to be called when mouse is clicked
    def printcoords(event):
        #outputting x and y coords to console
        print (event.x,event.y)
        pix = img.load()
        color =  '#%02x%02x%02x' % pix[event.x,event.y]
        print color
        
        canvas.create_rectangle(event.x -2, event.y -2, event.x + 2, event.y + 2,outline="red", fill="red", width=2)
        canvas.create_line(event.x, event.y, event.x + 20, event.y + 5,fill="red")
        canvas.create_rectangle(event.x + 20, event.y +5, event.x + 80, event.y + 25,outline="red", fill="white", width=1)
        canvas.create_text(event.x + 20, event.y + 10, anchor="nw",fill="red",text=color)
        # canvas.itemconfig(canvas_id, text=color)
        # canvas.insert(canvas_id, 12)
    #mouseclick event
    def save(event):
        print 'save'
        # canvas.postscript(file="circles.eps") # save canvas as encapsulated postscript
        # child = os.system("mogrify -format jpg circles.eps") # convert eps to jpg with ImageMagick
        ps = canvas.postscript(colormode='color')
        img = Image.open(io.BytesIO(ps.encode('utf-8')))
        img.save('test.jpg')

    canvas.bind("<Button-1>",printcoords)
    canvas.bind("<Button-2>",save)

    root.mainloop()