# -*- coding: utf-8 -*-
"""
Created on Fri Nov 01 21:48:03 2013

@author: lenovo
"""

from Tkinter import *
import random 
class SnakeGame:
    

    def __init__(self):
        self.foodx=5
        self.foody=5              
        self.score_level=0
        # moving step for snake and food
        self.step=15
        # game score
        self.gamescore=-10
        
        # to initialize the snake in the range of (x1,y1,x2,y1)                
        r=random.randrange(190,350,self.step)/15*15
        self.snakeX=[r,r+self.step,r+self.step*2]
        self.snakeY=[r,r,r]
        
        # to initialize the moving direction
        self.snakeDirection = 'left'  
        self.snakeMove = [-1,0]
        # to draw the game frame 
        self.window = Tk()
        self.window.geometry("600x400+10+10")
        self.window.maxsize(600,400)
        self.window.minsize(600,400)
        self.window.title("Snake game")
        
        self.frame1=Frame(self.window,bg='white')
        self.frame2=Frame(self.window,bg='white')
        self.canvas=Canvas(self.window,bg="green",width = 600, height = 360)
        self.score_label=Label(self.window,text="score"+'0',anchor='w')
        self.level_label=Label(self.window,text="score_level"+'1',anchor='e')
        
        self.frame1.pack()
        self.frame2.pack(fill=BOTH)        
        self.canvas.pack(fill=BOTH)
        self.score_label.pack(side=LEFT)
        self.level_label.pack(side=RIGHT)
         
        self.draw_wall()
        self.draw_score()
        self.draw_food()
        self.draw_snake()
        
        self.play()
        
        self.window.mainloop()

    "=== View Part ==="        
    def draw_wall(self):
        self.canvas.create_line(5,5,595,5,fill='purple',width=5)
        self.canvas.create_line(5,360,595,360,fill='purple',width=5)
        self.canvas.create_line(5,5,5,360,fill='purple',width=5)
        self.canvas.create_line(595,5,595,360,fill='purple',width=5)
        
    def draw_score(self):
        self.score()                        # score model
        self.score_label.config(self.score_label,text=self.gamescore)
        self.level_label.config(text='Level :'+str(self.gamescore/100+1))
        
    def draw_food(self):
        self.canvas.delete("food")
        self.foodx,self.foody=self.random_food()    #food model
        self.canvas.create_rectangle(self.foodx,self.foody,self.foodx+self.step,self.foody+self.step,fill='black' ,tags="food")     #food view
        
    def draw_snake(self):
        self.canvas.delete("snake")
        x,y=self.snake()                    # snake model
        for i in range(len(x)):             # snake view
            self.canvas.create_rectangle(x[i],y[i],x[i]+self.step,y[i]+self.step\
            , fill="blue",tags='snake')    
    
    "=== Model Part ==="
    # food model
    def random_food(self):      
        return(random.randrange(11,550,self.step)/15*15,random.randrange(11,340,self.step)/15*15)
    
    # snake model
    def snake(self):
        for i in range(len(self.snakeX)-1,0,-1):
            self.snakeX[i] = self.snakeX[i-1]
            self.snakeY[i] = self.snakeY[i-1]
        self.snakeX[0] += self.snakeMove[0]*self.step
        self.snakeY[0] += self.snakeMove[1]*self.step
        return(self.snakeX,self.snakeY)
        
    #score model    
    def score(self):
        if self.iseated:
           self.gamescore+=10

        
    
    "=== Control Part ==="     
    def iseated(self):
            if self.snakeX[0]==self.foodx and self.snakeY[0]==self.foody:
                return True
            else:   
                return False
    
    def isdead(self):
        if self.snakeX[0]<0 or self.snakeX[0] >599 or\
        self.snakeY[0]<0 or self.snakeY[0]>359 :
            return True
        
        for i in range(1,len(self.snakeX)):
            if self.snakeX[0]==self.snakeX[i] and self.snakeY[0]==self.snakeY[i] :
                return True
        else:
            return False
    
    def move(self,event):
    # left:[-1,0],right:[1,0],up:[0,1],down:[0,-1] 
        if (event.keycode == 39 or event.keycode == 68) and self.snakeDirection != 'left':
            self.snakeMove = [1,0]
            self.snakeDirection = "right"
        elif (event.keycode == 38 or event.keycode == 87) and self.snakeDirection != 'down':
            self.snakeMove = [0,-1]
            self.snakeDirection = "up"
        elif (event.keycode == 37 or event.keycode == 65) and self.snakeDirection != 'right':
            self.snakeMove = [-1,0]
            self.snakeDirection = "left"
        elif (event.keycode == 40 or event.keycode == 83) and self.snakeDirection != 'up':
            self.snakeMove = [0,1]
            self.snakeDirection = "down"
        else:
            pass

#       above codes can be insteaded by the following codes 
        
#        if (event.keysym == 'Right' or event.keysym == 'd') and self.snakeDirection != 'left':
#            self.snakeMove = [1,0]
#            self.snakeDirection = "right"
#        elif (event.keysym == 'Up' or event.keysym == 'w') and self.snakeDirection != 'down':
#            self.snakeMove = [0,-1]
#            self.snakeDirection = "up"
#        elif (event.keysym == 'Left' or event.keysym == 'a') and self.snakeDirection != 'right':
#            self.snakeMove = [-1,0]
#            self.snakeDirection = "left"
#        elif (event.keysym == 'Down' or event.keysym == 's') and self.snakeDirection != 'up':
#            self.snakeMove = [0,1]
#            self.snakeDirection = "down"
#        else:
#            pass
             
    def play(self):
        self.canvas.bind("<Key>",self.move)
        self.canvas.focus_set()

        while True:           
            if self.isdead():
                self.gameover()
                break
            elif self.iseated():
                #self.snakeX[0] += self.snakeMove[0]*self.step
                #self.snakeY[0] += self.snakeMove[1]*self.step   
                self.snakeX.insert(0,self.foodx)
                self.snakeY.insert(0,self.foody)                                 
                
                self.draw_score()
                self.draw_food()
                self.draw_snake()
            else:
                self.draw_snake() 
                self.canvas.after(100-10*(self.gamescore/100))
                self.canvas.update()
        
    def gameover(self):
        self.canvas.delete("food","snake")
        self.canvas.unbind('<Key>')
        self.canvas.bind("<Key>",self.restart)
        self.canvas.create_text(270,180,text="                   Game Over!\n \
        Press any key to continue",font='Helvetica -30 bold',tags='text')

    def restart(self,event):
        self.canvas.delete("food","snake","text")
        self.canvas.unbind('<Key>')

        # to initialize the snake in the range of (191,191,341,341)                
        r=random.randrange(191,191+15*10,self.step)/15*15
        self.snakeX=[r,r+self.step,r+self.step*2]
        self.snakeY=[r,r,r]
        
        # to initialize the moving direction
        self.snakeDirection = 'left'  
        self.snakeMove = [-1,0]
        
        # reset the score to zero 
        self.gamescore= -10
        self.draw_score() 
        
        # to initialize the game (food and snake)
        self.draw_food()
        self.draw_snake()
        
        # to play the game
        self.play()
        
SnakeGame()