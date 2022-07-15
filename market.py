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

    def step1():
        Window.p1_progress['value'] += 20
    def step2():
        Window.p2_progress['value'] += 20
    def step3():
        Window.p3_progress['value'] += 20
    def step4():
        Window.p4_progress['value'] += 20
    def step5():
        Window.p5_progress['value'] += 20
    def step6():
        Window.my_progress['value'] += 20

    def changeText():
        Window.price['text'] = 'Bought'
    def changeText2():
        Window.price2['text'] = 'Bought'
    def changeText3():
        Window.price3['text'] = 'Bought'
    def changeText4():
        Window.price4['text'] = 'Bought'
    def changeText5():
        Window.price5['text'] = 'Bought'
    def changeText6():
        Window.price6['text'] = 'Bought'

        Window.my_canvas.create_rectangle(10, 120, 500, 10, fill='grey')
        Window.my_canvas.create_text(50, 20, fill='black', font='Arial', text='Item Name')
        Window.my_canvas.create_text(75, 65, fill='black', font='Arial 15', text='Item Description')
        p1_progress = ttk.Progressbar(Window.my_canvas, orient=HORIZONTAL, length=300, mode='determinate')
        p1_progress.place(x= 100, y= 100)
        price = Button(Window.my_canvas, text='Price1', command=lambda:[Window.step1, Window.changeText], borderwidth=0)
        price.place(x=420, y=25)
        
        Window.my_canvas.create_rectangle(10, 250, 500, 125, fill='grey')
        Window.my_canvas.create_text(50, 135, fill='black', font='Arial', text='Item Name')
        Window.my_canvas.create_text(75, 180, fill='black', font='Arial 15', text='Item Description')
        p2_progress = ttk.Progressbar(Window.my_canvas, orient=HORIZONTAL, length=300, mode='determinate')
        p2_progress.place(x=100 , y=230)
        price2 = Button(Window.my_canvas, text='Price2', command=lambda:[Window.step2(), Window.changeText2], borderwidth=0)
        price2.place(x=420, y=150)
        

        Window.my_canvas.create_rectangle(10, 380, 500, 255, fill='grey')
        Window.my_canvas.create_text(50, 265, fill='blue', font='Arial', text='Item Name')
        Window.my_canvas.create_text(75, 300, fill='blue', font='Arial 15', text='Item Description')
        p3_progress = ttk.Progressbar(Window.my_canvas, orient=HORIZONTAL, length=300, mode='determinate')
        p3_progress.place(x=100, y=360)
        price3 = Button(Window.my_canvas, text='Price3', command=Window.changeText3, borderwidth=0)
        price3.place(x=420, y=270)

        Window.my_canvas.create_rectangle(10, 500, 500, 385, fill='grey')
        Window.my_canvas.create_text(50, 400, fill='red', font='Arial', text='Item Name')
        Window.my_canvas.create_text(75, 435, fill='red', font='Arial 15', text='Item Description')
        price4 = Button(Window.my_canvas, text='Price4', command=Window.changeText4, borderwidth=0)
        price4.place(x=420, y= 400)

        Window.my_canvas.create_rectangle(10, 505, 500, 645, fill='grey')
        Window.my_canvas.create_text(50, 665, fill='black', font='Arial', text='Item Name')
        Window.my_canvas.create_text(75, 700, fill='black', font='Arial 15', text='Item Description')
        price5 = Button(Window.my_canvas, text='Price5', command=Window.changeText5, borderwidth=0)
        price5.place(x=420, y=530)

        Window.my_canvas.create_rectangle(10, 650, 500, 780, fill='grey')
        Window.my_canvas.create_text(50, 520, fill='green', font='Arial', text='Item Name')
        Window.my_canvas.create_text(75, 570, fill='green', font='Arial 15', text='Item Description')
        price6 = Button(Window.my_canvas, text='Price6', command=None, borderwidth=0)
        price6.place(x=420, y=660)

        my_progress = ttk.Progressbar(Window.my_canvas, orient=HORIZONTAL,
            length=300, mode='determinate')
        my_progress.place(x= 300, y= 550)
        my_button = Button(Window.my_canvas, text='Progress', command=lambda:[Window.step(), Window.changeText5()])
        my_button.place(x= 420, y= 700)

        def close_window():
            Window.root.destroy()
        
        exitButton2 = Button(Window.my_canvas, text='Exit', command= close_window)
        exitButton2.place(x=420, y=700)
    
       
        Window.root.mainloop()