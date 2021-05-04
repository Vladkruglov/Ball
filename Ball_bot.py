from tkinter import Canvas, Tk
import random
import time
class Ball:
    def __init__(self, canvas, paddle1, paddle2, color):
        "Initialize ball settings"
        self.canvas = canvas
        self.paddle1 = paddle1
        self.id = canvas.create_oval(-7.5, -7.5, 7.5, 7.5, fill=color, outline="DarkOrange4")
        self.canvas.move(self.id, 250, 350)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x1 = starts[0]
        clor = [-1.5, 1.5]
        self.side = 'BLACK'
        self.y1 = random.choice(clor)
        if self.y1 == 1.5:
            self.side = 'RED'
        self.canvas_height = self.canvas.winfo_height()
        self.paddle2 = paddle2
        self.hit_red = False
        self.hit_blu = False
        self.canvas_width = self.canvas.winfo_width()
    def hit_paddle1(self, pos):
        "Locates paddle1 hits"
        paddle_pos = self.canvas.coords(self.paddle1.id)             
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:          
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
    def hit_paddle2(self, pos):
        "Locates paddle2 hits"
        paddle_pos = self.canvas.coords(self.paddle2.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[1] <= paddle_pos[3] and pos[1] >= paddle_pos[1]:
                return True
    def draw(self):
        "Draws ball"
        self.canvas.move(self.id, self.x1, self.y1)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y1 = 3
        if pos[3] >= self.canvas_height:
            self.hit_red = True
        if pos[1] <= 0:
            self.hit_blu = True
        if self.hit_paddle1(pos) == True:
            self.y1 = -3
        if self.hit_paddle2(pos) == True:
            self.y1 = 3
        if pos[0] <= 0:
            self.x1 = 3
        if pos[2] >= self.canvas_width:
            self.x1 = -3

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

        
class Paddle1:
    def __init__(self, canvas, color):
        "Initialize paddle1 settings"
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 5, fill=color, outline="darkred")
        self.canvas.move(self.id, 200, 672)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left1)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right1)
    def draw(self):
        "Draws RED paddle"
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0
    def turn_left1(self, evt):
        "Moves paddle left"
        self.x = -3
    def turn_right1(self, evt):
        "Moves paddle right"
        self.x = 3

class Paddle2:
    def __init__(self, canvas, color):
        "Initialize BLU team paddle"
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 5, fill=color, outline="black")
        self.canvas.move(self.id, 200, 28)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
    def draw(self):
        "Draws BLU paddle"
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0
    def turn_left1(self):
        "Turns paddle left"
        self.x = -3
    def turn_right1(self):
        "Turns paddle right"
        self.x = 3
    def kick_easy(self, ball):
        ball_pos = list(canvas.coords(ball.id))
        pad_pos = list(canvas.coords(self.id))    
        ran = random.randint(0,25)    
        if ran == 25:
            for i in range(0,10):
                self.x = 0   

        elif ball_pos[0] < pad_pos[0]:
            self.turn_left1()

        elif ball_pos[2] > pad_pos[2]:
            self.turn_right1()

    def kick_medium(self, ball):
        ball_pos = list(canvas.coords(ball.id))
        pad_pos = list(canvas.coords(self.id))    
        ran = random.randint(0,50)    
        if ran == 50:
            for i in range(0,10):
                self.x = 0   

        elif ball_pos[0] < pad_pos[0]:
            self.turn_left1()

        elif ball_pos[2] > pad_pos[2]:
            self.turn_right1()

    def kick_high(self, ball):
        ball_pos = list(canvas.coords(ball.id))
        pad_pos = list(canvas.coords(self.id))    
        ran = random.randint(0,100)    
        if ran == 100:
            for i in range(0,10):
                self.x = 0   

        elif ball_pos[0] < pad_pos[0]:
            self.turn_left1()

        elif ball_pos[2] > pad_pos[2]:
            self.turn_right1()

    def kick_imp(self, ball):
        ball_pos = list(canvas.coords(ball.id))
        pad_pos = list(canvas.coords(self.id))     
        if ball_pos[0] < pad_pos[0]:
            self.turn_left1()

        elif ball_pos[2] > pad_pos[2]:
            self.turn_right1()
                                                           

dif = input("Select level(e, m, h, i): ")
tk = Tk()
tk.title("Ping Pong!")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=700, bd=0,
highlightthickness=0, background = "dodgerblue")
canvas.pack()
tk.update()
canvas.create_rectangle(0, 345, 700, 355, fill='white', outline = 'white')
canvas.create_rectangle(0, 0, 5, 700, fill='white', outline = 'white')
canvas.create_rectangle(495, 0, 500, 700, fill='white', outline = 'white')
canvas.create_rectangle(245, 700, 255, 0, fill='white', outline = 'white')
canvas.create_rectangle(0, 349, 700, 351, fill='black', outline = 'black')
canvas.create_rectangle(0, 695, 700, 700, fill='white', outline = 'white')
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
        elif dif == "i":
            paddle2.kick_imp(ball)
        paddle2.draw()
        tk.update_idletasks()
        tk.update()
        time.sleep(time_pl)
        time_p = int(time.time() - tim)
        time_pl = time_pl - 0.000000001
        # canvas.create_rectangle(0, 0, 70, 30, fill="lightblue", outline="lightblue")
        # canvas.create_text(30, 10, text=coun)
        # canvas.create_text(30, 25, text=time_play)
        # canvas.()
    elif ball.hit_red == True or ball.hit_blu == True:
        print("GAME OVER")
        if ball.hit_blu == True:
            print("RED IS THE WINNER!!!")
        elif ball.hit_red == True:
            print("BLACK IS THE WINNER!!!")
        print("Time played: {} secs".format(int(time_p)))
        print("Hits RED: {}".format(int(coured)))
        print("Hits BLACK: {}".format(int(coublu)))
        time.sleep(2.5)
        break
