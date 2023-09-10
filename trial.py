import tkinter as tk
import random

class FlappyBird:
    def __init__(self, master):
        self.master = master
        self.master.title("Flappy Bird")
        self.master.geometry("500x600")
        self.master.resizable(False, False)

        self.canvas = tk.Canvas(self.master, bg="sky blue", width=500, height=500)
        self.canvas.pack()

        self.bird = self.canvas.create_oval(50, 250, 70, 270, fill="yellow")

        self.pipes = []
        self.pipe_speed = 4
        self.pipe_width = 70
        self.pipe_gap = 120
        self.pipe_distance = 200

        self.score = 0
        self.score_label = tk.Label(self.master, text="Score: 0", font=("Arial", 20), bg="sky blue")
        self.score_label.pack()

        self.master.bind("<space>", self.jump)
        self.master.bind("<Up>", self.jump)
        self.master.bind("<Button-1>", self.jump)

        self.update()

    def update(self):
        self.move_bird()
        self.move_pipes()
        self.check_collision()
        self.check_score()

        self.master.after(10, self.update)

    def move_bird(self):
        self.canvas.move(self.bird, 0, 3)

    def jump(self, event):
        self.canvas.move(self.bird, 0, -60)

    def move_pipes(self):
        for pipe in self.pipes:
            self.canvas.move(pipe, -self.pipe_speed, 0)

        if len(self.pipes) == 0 or self.canvas.coords(self.pipes[-1])[2] < 500 - self.pipe_distance:
            top_pipe_height = random.randint(50, 250)
            bottom_pipe_height = 500 - self.pipe_gap - top_pipe_height

            top_pipe = self.canvas.create_rectangle(500, 0, 500 + self.pipe_width, top_pipe_height, fill="green")
            bottom_pipe = self.canvas.create_rectangle(500, 500, 500 + self.pipe_width, bottom_pipe_height, fill="green")

            self.pipes.append(top_pipe)
            self.pipes.append(bottom_pipe)

        if self.canvas.coords(self.pipes[0])[2] < 0:
            self.canvas.delete(self.pipes.pop(0))
            self.canvas.delete(self.pipes.pop(0))

    def check_collision(self):
        bird_coords = self.canvas.coords(self.bird)

        if bird_coords[1] < 0 or bird_coords[3] > 500:
            self.game_over()

        for pipe in self.pipes:
            pipe_coords = self.canvas.coords(pipe)

            if (bird_coords[0] + 10 < pipe_coords[2] and bird_coords[2] - 10 > pipe_coords[0] and
                    (bird_coords[1] + 10 < pipe_coords[1] or bird_coords[3] - 10 > pipe_coords[3])):
                self.game_over()

    def check_score(self):
        if len(self.pipes) > 0 and self.canvas.coords(self.pipes[0])[2] < 50:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")

    def game_over(self):
        self.canvas.delete("all")
        self.canvas.create_text(250, 250, text="Game Over", font=("Arial", 40), fill="red")
        self.canvas.create_text(250, 350, text=f"Final Score: {self.score}")

root = tk.Tk()
myapp = FlappyBird(root)
root.mainloop()
