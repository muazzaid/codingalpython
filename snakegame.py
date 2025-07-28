from tkinter import *
from random import randint
#from PIL import Image, ImageTk

movement = 40
steps_per_second = 20
speed = 1200// steps_per_second

class Snake(Canvas):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.direction = 'Right'
        self.food_position = self.place_food()
        self.score = 0
        self.create_widgets()
        self.bind("<KeyPress>", self.change_direction)
        self.after(speed, self.move_snake)

    def create_widgets(self):
        self.pack(fill=BOTH, expand=True)
        self.focus_set()
        self.draw_snake()
        self.draw_food()

    def draw_snake(self):
        for segment in self.snake:
            x, y = segment
            self.create_rectangle(x, y, x + 20, y + 20, fill='green')

    def draw_food(self):
        x, y = self.food_position
        self.create_oval(x, y, x + 20, y + 20, fill='red')

    def place_food(self):
        x = randint(0, (self.winfo_width() // 20) - 1) * 20
        y = randint(0, (self.winfo_height() // 20) - 1) * 20
        return (x, y)

    def change_direction(self, event):
        if event.keysym in ['Up', 'Down', 'Left', 'Right']:
            if (event.keysym == 'Up' and self.direction != 'Down') or \
               (event.keysym == 'Down' and self.direction != 'Up') or \
               (event.keysym == 'Left' and self.direction != 'Right') or \
               (event.keysym == 'Right' and self.direction != 'Left'):
                self.direction = event.keysym

    def move_snake(self):
        head_x, head_y = self.snake[0]
        
        if self.direction == 'Up':
            new_head = (head_x, head_y - movement)
        elif self.direction == 'Down':
            new_head = (head_x, head_y + movement)
        elif self.direction == 'Left':
            new_head = (head_x - movement, head_y)
        elif self.direction == 'Right':
            new_head = (head_x + movement, head_y)

        if new_head in self.snake or \
           new_head[0]  < 0 or new_head[0] >= self.winfo_width() or  new_head[1] < 0 or new_head[1] >= self.winfo_height():
            self.game_over()
            return

        self.snake.insert(0, new_head)

        if new_head == self.food_position:
            self.score += 1
            self.food_position = self.place_food()
            self.draw_food()
        else:
            tail = self.snake.pop()
            self.delete(self.find_closest(tail[0] + 10, tail[1] + 10))

        self.draw_snake()
        self.after(speed, self.move_snake)

    def game_over(self):
        self.create_text(self.winfo_width() // 2, 
                         self.winfo_height() // 2, 
                         text="Game Over", fill="red", font=("Arial", 24))
        self.unbind("<KeyPress>")
window.
