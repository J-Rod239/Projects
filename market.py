from tkinter import*
from tkinter import ttk
import tkinter as tk

class Window():
    def opener():
        Window.root = Tk()
        Window.root.geometry('510x800')
        Window.root.title('Market')
        Window.root.resizable(False, False)

        Window.main_frame = Frame(Window.root, bg='blue')
        Window.main_frame.pack(expand=True, fill=BOTH)

        Window.my_canvas = Canvas(Window.main_frame, width=510, height=800, bg='white')
        Window.my_canvas.pack(side=LEFT, fill=BOTH, expand=True)

        Window.secondFrame = Frame(Window.my_canvas)
        Window.my_canvas.create_window((0,0), window=Window.secondFrame)
        
        #Window.img = PhotoImage(file='//Users//projose239//Documents//GitHub//Capstone-Proj//artwork-fillip//cape.PNG')

        #Window.my_canvas.create_image(10, 10, anchor=NE, image= Window.opener.img)
        Window.my_canvas.create_rectangle(10, 120, 500, 10, fill='grey')
        Window.my_canvas.create_text(50, 20, fill='black', font='Arial', text='Item Name')
        Window.my_canvas.create_text(75, 65, fill='black', font='Arial 15', text='Item Description')
        price = Button(Window.my_canvas, text='Price1', command=None, borderwidth=0)
        price.place(x=420, y=25)
        
        Window.my_canvas.create_rectangle(10, 250, 500, 125, fill='grey')
        Window.my_canvas.create_text(50, 135, fill='black', font='Arial', text='Item Name')
        Window.my_canvas.create_text(75, 180, fill='black', font='Arial 15', text='Item Description')
        price2 = Button(Window.my_canvas, text='Price2', command=None, borderwidth=0)
        price2.place(x=420, y=150)

        Window.my_canvas.create_rectangle(10, 380, 500, 255, fill='grey')
        Window.my_canvas.create_text(50, 265, fill='blue', font='Arial', text='Item Name')
        Window.my_canvas.create_text(75, 300, fill='blue', font='Arial 15', text='Item Description')
        price3 = Button(Window.my_canvas, text='Price3', command=None, borderwidth=0)
        price3.place(x=420, y=270)

        Window.my_canvas.create_rectangle(10, 500, 500, 385, fill='grey')
        Window.my_canvas.create_text(50, 400, fill='red', font='Arial', text='Item Name')
        Window.my_canvas.create_text(75, 435, fill='red', font='Arial 15', text='Item Description')
        price4 = Button(Window.my_canvas, text='Price4', command=None, borderwidth=0)
        price4.place(x=420, y= 400)

        Window.my_canvas.create_rectangle(10, 505, 500, 645, fill='grey')
        Window.my_canvas.create_text(50, 665, fill='black', font='Arial', text='Item Name')
        Window.my_canvas.create_text(75, 700, fill='black', font='Arial 15', text='Item Description')
        price5 = Button(Window.my_canvas, text='Price5', command=None, borderwidth=0)
        price5.place(x=420, y=530)

        Window.my_canvas.create_rectangle(10, 650, 500, 780, fill='grey')
        Window.my_canvas.create_text(50, 520, fill='green', font='Arial', text='Item Name')
        Window.my_canvas.create_text(75, 570, fill='green', font='Arial 15', text='Item Description')
        price6 = Button(Window.my_canvas, text='Price6', command=None, borderwidth=0)
        price6.pack(padx=35, pady=790, anchor=E)
    
        Window.root.mainloop()


    #Window.opener.my_canvas.create_rectangle(10, 790, 500, 880, fill='grey')
   

