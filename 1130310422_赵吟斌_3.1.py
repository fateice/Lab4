# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 14:21:54 2013

@author: Kimi
"""
from Tkinter import *   #import Tkinter model

class experiment:    #create a class    
    def __init__(self):   
        self.window=Tk()        #creat a window
        self.window.title("EX3.3.1")        #set title
        self.window.geometry("400x300")         #set the size of the window
        self.label = Label(self.window, text = "Widgets")       #set the label
        self.canvas = Canvas(self.window, bg = "white", width = 400, height = 250)      #create the canvas set it's color,window 
        self.button = Button(self.window,text="Rectangle",command = self.appear)        #create a button, set it's function
        self.canvas.bind("<Key>",self.keyboard_input)       #check if there is a keyboard input
        self.canvas.focus_set()     #Initialize     
        self.t=""           #Initialize
        
        self.label.pack()       #pack the label
        self.canvas.pack()        #pack the canvas
        self.button.pack()        #pack the button
        self.window.mainloop()        
        
    def appear(self):   #define a button event
        self.canvas.create_rectangle(140,80,240,180,fill="red",tags="E3")   #create a red rectangular
        self.t=""        #Initialize
        self.canvas.delete("E5")      #delete text
        self.label.config(self.label,text="Mouse Event")    #change the label
    
    def keyboard_input(self,event):     #define a keyboard event              
        i=event.char        
        self.canvas.delete("E3")    #delete red canvas
        self.t=self.t+i     
        self.label.config(self.label,text="Keyboard Event")  #change lable
        self.canvas.create_text((100,100), anchor="nw",text=self.t,tags="E5")   #the location of the text,print text
experiment()           
