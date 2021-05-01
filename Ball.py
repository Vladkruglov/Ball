from tkinter import Canvas, Tk
import random
import time
class Ball:
    def __init__(self, canvas, paddle1, paddle2, color):
        self.canvas = canvas
        self.paddle1 = paddle1
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color, outline="darkgreen")
        self.canvas.move(self.id, 350, 350)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x1 = starts[0]
        clor = [-1.5, 1.5]
        self.y1 = random.choice(clor)
        self.canvas_height = self.canvas.winfo_height()
        self.paddle2 = paddle2
        self.hit_bottom = False
        self.canvas_width = self.canvas.winfo_width()
    def hit_paddle1(self, pos):
        paddle_pos = self.canvas.coords(self.paddle1.id)             
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:          
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
    def hit_paddle2(self, pos):
        paddle_pos = self.canvas.coords(self.paddle2.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[1] <= paddle_pos[1]:
                return True
    def draw(self):
        self.canvas.move(self.id, self.x1, self.y1)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y1 = 3
        if pos[3] >= self.canvas_height or pos[1] <= 0:
            self.hit_bottom = True
        if self.hit_paddle1(pos) == True:
            self.y1 = -3
        if self.hit_paddle2(pos) == True:
            self.y1 = 3
        if pos[0] <= 0:
            self.x1 = 3
        if pos[2] >= self.canvas_width:
            self.x1 = -3

    def counter(self, cou):
        pos = self.canvas.coords(self.id)
        if self.hit_paddle1(pos) == True:
            cou = cou + 1
        return cou

        
class Paddle1:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 5, fill=color, outline="darkred")
        self.canvas.move(self.id, 350, 672)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left1)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right1)
    def pause(self, evt):
        time.sleep(0.0000001)
    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0
    def turn_left1(self, evt):
        self.x = -3
    def turn_right1(self, evt):
        self.x = 3

class Paddle2:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 5, fill=color, outline="darkblue")
        self.canvas.move(self.id, 350, 28)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('a', self.turn_left1)
        self.canvas.bind_all('d', self.turn_right1)
    def pause(self, evt):
        time.sleep(0.0000001)
    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0
    def turn_left1(self, evt):
        self.x = -3
    def turn_right1(self, evt):
        self.x = 3

tk = Tk()
tk.title("Игра")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=700, height=700, bd=0,
highlightthickness=0, background = "lightblue")
canvas.pack()
tk.update()
tim = time.time()
time_pl = 0.01
paddle1 = Paddle1(canvas, 'red')
paddle2 = Paddle2(canvas, 'blue')
ball = Ball(canvas, paddle1,paddle2, '#00ff00')
cou = 0 
ball.draw()
cou = ball.counter(cou)
paddle1.draw()
paddle2.draw()
tk.update_idletasks()
tk.update()
time.sleep(5)
while True:
    if ball.hit_bottom == False:
        ball.draw()
        cou = ball.counter(cou)
        paddle1.draw()
        paddle2.draw()
        tk.update_idletasks()
        tk.update()
        time.sleep(time_pl)
        time_p = int(time.time() - tim)
        coun = "Hits: {}".format(cou)
        time_play = "Time: {}".format(time_p)
        # canvas.create_rectangle(0, 0, 70, 30, fill="lightblue", outline="lightblue")
        # canvas.create_text(30, 10, text=coun)
        # canvas.create_text(30, 25, text=time_play)
        # canvas.()
    elif ball.hit_bottom == True:
        print("GAME OVER")
        print("Time played: {} secs".format(int(time_p)))
        print("Hits: {}".format(int(cou)))
        time.sleep(2.5)
        break
