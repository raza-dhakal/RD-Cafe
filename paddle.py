import tkinter as tk
from tkinter import messagebox
import time

# मुख्य विन्डो तयार गर्नुहोस्
window = tk.Tk()
window.title("Pong Game")
window.resizable(False, False)

# स्क्रीन साइज सेटअप
WIDTH, HEIGHT = 800, 600
canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

# खेलका फिचरहरू
PADDLE_COLOR = "white"
BALL_COLOR = "white"

# प्याडल र बलको साइज
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 10
BALL_SIZE = 20

# तलको प्याडल (Bottom Paddle)
bottom_paddle = canvas.create_rectangle(
    WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - 30,
    WIDTH // 2 + PADDLE_WIDTH // 2, HEIGHT - 30 + PADDLE_HEIGHT,
    fill=PADDLE_COLOR
)

# बल (Ball)
ball = canvas.create_oval(
    WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2,
    WIDTH // 2 + BALL_SIZE // 2, HEIGHT // 2 + BALL_SIZE // 2,
    fill=BALL_COLOR
)

# गति सेटअप
paddle_speed = 0
ball_speed_x = 5
ball_speed_y = 5

# कीबोर्ड इनपुट ह्यान्डल गर्नुहोस्
def move_paddle(event):
    global paddle_speed
    if event.keysym == "Left":
        paddle_speed = -7
    elif event.keysym == "Right":
        paddle_speed = 7

def stop_paddle(event):
    global paddle_speed
    if event.keysym in ("Left", "Right"):
        paddle_speed = 0

window.bind("<KeyPress>", move_paddle)
window.bind("<KeyRelease>", stop_paddle)

# खेल पुनः सुरु गर्ने फङ्क्सन
def reset_game():
    global ball_speed_x, ball_speed_y
    canvas.coords(bottom_paddle, WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - 30,
                  WIDTH // 2 + PADDLE_WIDTH // 2, HEIGHT - 30 + PADDLE_HEIGHT)
    canvas.coords(ball, WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2,
                  WIDTH // 2 + BALL_SIZE // 2, HEIGHT // 2 + BALL_SIZE // 2)
    ball_speed_x = 5
    ball_speed_y = 5
    start_game_button.pack_forget()  # Start बटन लुकाउनुहोस्
    update_game()

# खेल अपडेट गर्ने फङ्क्सन
def update_game():
    global ball_speed_x, ball_speed_y

    # प्याडलको गति
    canvas.move(bottom_paddle, paddle_speed, 0)

    # प्याडलको सिमाना चेक गर्नुहोस्
    paddle_coords = canvas.coords(bottom_paddle)
    if paddle_coords[0] <= 0:
        canvas.move(bottom_paddle, -paddle_coords[0], 0)
    elif paddle_coords[2] >= WIDTH:
        canvas.move(bottom_paddle, WIDTH - paddle_coords[2], 0)

    # बलको गति
    canvas.move(ball, ball_speed_x, ball_speed_y)
    ball_coords = canvas.coords(ball)

    # बल माथि/साइड सिमानामा ठोक्किँदा दिशा बदल्नुहोस्
    if ball_coords[0] <= 0 or ball_coords[2] >= WIDTH:
        ball_speed_x *= -1
    if ball_coords[1] <= 0:
        ball_speed_y *= -1

    # बल तलको प्याडलसँग ठोक्किए
    if ball_coords[3] >= paddle_coords[1] and \
       paddle_coords[0] <= ball_coords[0] <= paddle_coords[2]:
        ball_speed_y *= -1

    # बल तल पुग्यो भने खेल समाप्त
    if ball_coords[3] >= HEIGHT:
        game_over()
        return

    # फङ्क्सनलाई पुन: बोलाउनुहोस्
    window.after(16, update_game)

# खेल समाप्त हुने फङ्क्सन
def game_over():
    messagebox.showinfo("Game Over", "Game Over! Click 'Start a Game' to play again.")
    start_game_button.pack()  # Start बटन देखाउनुहोस्

# खेल सुरु गर्न बटन
start_game_button = tk.Button(window, text="Start a Game", command=reset_game, font=("Arial", 14))
start_game_button.pack()

# खेल सुरु गर्नुहोस्
reset_game()
window.mainloop()
