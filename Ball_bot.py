from tkinter import Canvas, Tk
# import pygame
import random
import time
class Ball:
    def __init__(self, canvas, paddle1, paddle2, color):
        "Initialize ball settings"
        self.canvas = canvas
        self.paddle1 = paddle1
        self.id = canvas.create_oval(-7.5, -7.5, 7.5, 7.5, fill=color, outline="DarkOrange4")
        self.canvas.move(self.id, 350, 225)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.y1 = starts[0]
        clor = [-1.5, 1.5]
        self.side = 'BLACK'
        self.x1 = random.choice(clor)
        if self.x1 == 1.5:
            self.side = 'RED'
        self.canvas_height = self.canvas.winfo_height()
        self.paddle2 = paddle2
        self.hit_red = False
        self.hit_blu = False
        self.canvas_width = self.canvas.winfo_width()
    def hit_paddle1(self, pos):
        "Locates paddle1 hits"
        paddle_pos = self.canvas.coords(self.paddle1.id)             
        if pos[3] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:          
            if pos[2] >= paddle_pos[0] and pos[2] <= paddle_pos[2]:
                return True
    def hit_paddle2(self, pos):
        "Locates paddle2 hits"
        paddle_pos = self.canvas.coords(self.paddle2.id)
        if pos[3] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
            if pos[0] <= paddle_pos[2] and pos[0] >= paddle_pos[0]:
                return True
    def draw(self):
        "Draws ball"
        self.canvas.move(self.id, self.x1, self.y1)
        pos = self.canvas.coords(self.id)
        if pos[3] <= 0:
            self.x1 = 3
        if pos[0] >= self.canvas_width:
            self.hit_red = True
        if pos[2] <= 0:
            self.hit_blu = True
        if self.hit_paddle1(pos) == True:
            self.x1 = -3
        if self.hit_paddle2(pos) == True:
            self.x1 = 3
        if pos[1] <= 0:
            self.y1 = 3
        if pos[3] >= self.canvas_height:
            self.y1 = -3

    def counterred(self, cou):
        "Counts hits for RED team"
        pos = self.canvas.coords(self.id)
        if self.hit_paddle1(pos) == True:
            cou = cou + 1
        return cou
    
    def counterblu(self, cou):
        "Counts hits for BLU team"
        pos = self.canvas.coords(self.id)
        if self.hit_paddle2(pos) == True:
            cou = cou + 1
        return cou

    
    def sound(self, pyg):
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0 or pos[2] >= 400:
            pyg.mixer.init()
            pyg.mixer.music.load("Sounds/Стол1.mp3")
            pyg.mixer.music.play()
        if self.hit_paddle1 == True or self.hit_paddle2 == True:
            sounds = ["Sounds/Ракетка1.mp3", "Sounds/Ракетка2.mp3"]
            pyg.mixer.init()
            pyg.mixer.music.load(random.choice(sounds))
            pyg.mixer.music.play()
        


class Paddle1:
    def __init__(self, canvas, color):
        "Initialize paddle1 settings"
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 100, 5, 0, fill=color, outline="darkred")
        self.canvas.move(self.id, 672, 175)
        self.y = 0
        self.canvas_height = self.canvas.winfo_height()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left1)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right1)
    def draw(self):
        "Draws RED paddle"
        self.canvas.move(self.id, 0, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 0
        elif pos[3] >= self.canvas_height:
            self.y = 0
    def turn_left1(self, evt):
        "Moves paddle left"
        pos = canvas.coords(self.id)
        if pos[3] < 450:
            self.y = 3
        elif pos[3] >= 450:
            self.x = 0

    def turn_right1(self, evt):
        "Moves paddle right"
        pos = canvas.coords(self.id)
        if pos[1] > 0:
            self.y = -3
        elif pos[1] <= 0:
            self.x = 0

class Paddle2:
    def __init__(self, canvas, color):
        "Initialize paddle1 settings"
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 100, 5, 0, fill=color, outline="black")
        self.canvas.move(self.id, 18, 175)
        self.y = 0
        self.canvas_height = self.canvas.winfo_height()
    def draw(self):
        "Draws RED paddle"
        self.canvas.move(self.id, 0, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 0
        elif pos[3] >= self.canvas_height:
            self.y = 0
    def turn_left1(self):
        "Moves paddle left"
        pos = canvas.coords(self.id)
        if pos[1] > 0:
            self.y = -3
        elif pos[1] <= 0:
            self.y = 0

    def turn_right1(self):
        "Moves paddle right"
        pos = canvas.coords(self.id)
        if pos[3] < 450:
            self.y = 3
        elif pos[3] >= 450:
            self.y = 0    
    def kick_easy(self, ball):
        ball_pos = list(canvas.coords(ball.id))
        pad_pos = list(canvas.coords(self.id))    
        ran = random.randint(0,25)    
        if ran == 25:
            for i in range(0,10):
                self.y = 0   

        elif ball_pos[1] < pad_pos[1]:
            self.turn_left1()

        elif ball_pos[3] > pad_pos[3]:
            self.turn_right1()

    def kick_medium(self, ball):
        ball_pos = list(canvas.coords(ball.id))
        pad_pos = list(canvas.coords(self.id))    
        ran = random.randint(0,37)    
        if ran == 37:
            for i in range(0,10):
                self.y = 0   

        elif ball_pos[1] < pad_pos[1]:
            self.turn_left1()

        elif ball_pos[3] > pad_pos[3]:
            self.turn_right1()

    def kick_high(self, ball):
        ball_pos = list(canvas.coords(ball.id))
        pad_pos = list(canvas.coords(self.id))    
        ran = random.randint(0,50)    
        if ran == 50:
            for i in range(0,10):
                self.y = 0   

        elif ball_pos[1] < pad_pos[1]:
            self.turn_left1()

        elif ball_pos[3] > pad_pos[3]:
            self.turn_right1()

    def kick_imp(self, ball):
        ball_pos = list(canvas.coords(ball.id))
        pad_pos = list(canvas.coords(self.id))     
        if ball_pos[1] < pad_pos[1]:
            self.turn_left1()

        elif ball_pos[3] > pad_pos[3]:
            self.turn_right1()
                                                           

dif = input("Select level(e, m, h, i): ")
tk = Tk()
tk.title("Ping Pong!")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=700, height=450, bd=0,
highlightthickness=0, background = "dodgerblue")
canvas.pack()
tk.update()
canvas.create_rectangle(345, 0, 355, 700, fill='white', outline = 'white')
canvas.create_rectangle(0, 0, 5, 700, fill='white', outline = 'white')
canvas.create_rectangle(695, 0, 700, 700, fill='white', outline = 'white')
canvas.create_rectangle(700, 220, 0, 230, fill='white', outline = 'white')
canvas.create_rectangle(349, 0, 351, 700, fill='black', outline = 'black')
canvas.create_rectangle(0, 445, 700, 450, fill='white', outline = 'white')
canvas.create_rectangle(0, 5, 700, 0, fill='white', outline = 'white')
canvas.update()
canvas.update_idletasks()

time_pl = 0.01
paddle1 = Paddle1(canvas, 'red')
paddle2 = Paddle2(canvas, 'black')
ball = Ball(canvas, paddle1,paddle2, 'darkorange')
cou = 0 
ball.draw()
coured = ball.counterred(cou)
coublu = ball.counterblu(cou)
paddle1.draw()
paddle2.draw()
tk.update_idletasks()
tk.update()
time.sleep(5)
tim = time.time()
print("Started with: {}".format(ball.side))
while True:
    if ball.hit_red == False and ball.hit_blu == False:
        ball.draw()
        coured = ball.counterred(coured)
        coublu = ball.counterblu(coublu)
        paddle1.draw()
        if dif == "e":
            paddle2.kick_easy(ball)
        elif dif == "m":
            paddle2.kick_medium(ball)
        elif dif == "h":
            paddle2.kick_high(ball)
        elif dif == "i" or dif != 'e' and dif != 'm' and dif != 'h':
            paddle2.kick_imp(ball)
        paddle2.draw()
        tk.update_idletasks()
        tk.update()
        time.sleep(time_pl)
        time_p = int(time.time() - tim)
        time_pl = time_pl - 0.0000001
        # canvas.create_rectangle(0, 0, 70, 30, fill="lightblue", outline="lightblue")
        # canvas.create_text(30, 10, text=coun)
        # canvas.create_text(30, 25, text=time_play)
        # canvas.()
    elif ball.hit_red == True or ball.hit_blu == True:
        print("GAME OVER")
        if ball.hit_blu == True:
            for i in range(0,50):
                ball.y1 = -1
                ball.draw()
                paddle1.draw()
                paddle2.draw()
                tk.update_idletasks()
                tk.update()
                time.sleep(time_pl)
            print("RED IS THE WINNER!!!")
        elif ball.hit_red == True:
            for i in range(0,50):
                ball.y1 = 1
                ball.draw()
                paddle1.draw()
                if dif == "e":
                    paddle2.kick_easy(ball)
                elif dif == "m":
                    paddle2.kick_medium(ball)
                elif dif == "h":
                    paddle2.kick_high(ball)
                elif dif == "i" or dif != 'e' and dif != 'm' and dif != 'h':
                    paddle2.kick_imp(ball)
                paddle2.draw()
                tk.update_idletasks()
                tk.update()
                time.sleep(time_pl)
            print("BLACK IS THE WINNER!!!")
        print("Time played: {} secs".format(int(time_p)))
        print("Hits RED: {}".format(int(coured)))
        print("Hits BLACK: {}".format(int(coublu)))
        time.sleep(2.5)
        break        
        
