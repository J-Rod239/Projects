from logging import root
import sys
import os
path = '//Users//projose239//Documents//GitHub//Capstone-Proj//market.py'
sys.path.append(path)
import tkinter
from tkinter import*
import market

tkWindow =Tk()
#tkWindow.geometry('550x800')
tkWindow.geometry('1045x1920')
tkWindow.title('Mini Apes')

class Functions:
    

    def inventoryWindow():
        #This is the right way so that the window doesnt appear when first opening the program
    
        global invCount
       
        if invCount < 2:    
            newWindow= Toplevel()
            newWindow.geometry("1069x900")
            invlabel = Label(newWindow, text = "Inventory").pack()
            buttonExample = Button(newWindow, text= "Close Window", command=newWindow.destroy).pack()

        invCount +=1

    def statWindow():

        global statCount
    
        if statCount < 2:
            statBlock= Toplevel()
            statBlock.geometry("1069x900") 
            statlabel = Label(statBlock, text= "Stats Window").pack()
            statButton = Button(statBlock, text="Close Window", command=statBlock.destroy).pack()
    
        statCount +=1

    def marketWindow():
        global markCount
        
        if markCount < 2:
            market.Window.opener()
            market.Main()
            #exec(open('market.py').read(market.Window.opener))
            #marketBlock= Toplevel()
            #marketBlock.geometry("1069x900")
            #marketlabel = Label(marketBlock, text= "Market Window").pack()
            #marketButton = Button(marketBlock, text= "Close Window", command=marketBlock.destroy).pack()
    
        markCount +=1

    def settingWindow():

        global settCount

        if settCount < 2:
            settingBlock= Toplevel()
            settingBlock.geometry("1069x900")
            settlabel = Label(settingBlock, text= "Settings Window").pack()
            settingButton = Button(settingBlock, text= "Close Window", command=settingBlock.destroy).pack()

        settCount +=1

class Variables:
    global invCount
    global statCount
    global markCount
    global settCount 
    invCount = 1
    statCount = 1
    markCount = 1
    settCount = 1

class Images:
    #Images
    background = PhotoImage(file="//Users/projose239//Documents//Senior Capstone//background_art.png")
    label = Label(tkWindow, image=background)
    label.place(x=0, y=0)

    filip = PhotoImage(file="//Users//projose239//Documents//GitHub//Capstone-Proj//artwork-fillip//mini_apetransparent_png.png")
    labelfil = Label(tkWindow, image=filip)
    labelfil.place(x=210 , y=100)

    inv_button = PhotoImage(file= "//Users//projose239//Documents//Senior Capstone//Buttons//inventory.png")
    inv_label = Label(image=inv_button)

    stats_button = PhotoImage(file= "//Users/projose239//Documents//Senior Capstone//Buttons//stats.png")
    stats_label = Label(image=stats_button)

    market_button = PhotoImage(file= "//Users//projose239//Documents//Senior Capstone//Buttons//market.png")
    market_label = Label(image=market_button)

    set_button = PhotoImage(file= "//Users//projose239//Documents//Senior Capstone//Buttons//settings.png")
    img_label = Label(image=set_button)

    mine_button = PhotoImage(file= "//Users//projose239//Documents//Senior Capstone//Buttons//bottom_menu_MineTouch 2.png")
    mine_label = Label(image=mine_button)

class Buttons:
    #BUTTONS
    button1 = Button(tkWindow, image=Images.inv_button, command=Functions.inventoryWindow, borderwidth=0)
    button1.place(x=0.1, y=1045, anchor=tkinter.SW)

    button2 = Button(tkWindow, image=Images.stats_button, command=Functions.statWindow, borderwidth=0)
    button2.place(x=339, y=1045, anchor=tkinter.S)

    button3 = Button(tkWindow, image=Images.market_button, command=Functions.marketWindow, borderwidth=0)
    button3.place(x=848, y=1045, anchor=tkinter.SE)

    button4 = Button(tkWindow, image=Images.set_button, command=Functions.settingWindow, borderwidth=0)
    button4.place(x=1045, y=1045, anchor=tkinter.SE)

    mineButton = Button(tkWindow, image=Images.mine_button , command=None, borderwidth= 0)
    mineButton.place(x=380 , y=765)

def exitProgram(exitBtn):
    exitBtn.instance.destroy()
    
exitBtn = Button(text="Exit", command=tkWindow.destroy)
exitBtn.place(x=10, y= 100)
tkWindow.mainloop()