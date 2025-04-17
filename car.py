import tkinter
WIDTH, HEIGHT = 480, 720
bg_y = 0
p1_x = int(WIDTH/2)
p1_y = int(HEIGHT/2)

def move(e):
  global p1_x, p1_y
  p1_x = int(0.8*p1_x+0.2*e.x)
  p1_y = int(0.8*p1_y+0.2*e.y)
  if p1_x<160: p1_x = 160
  if p1_y<320: p1_y = 320
def main():
  global bg_y
  bg_y = bg_y + 2
  if bg_y>=HEIGHT: bg_y = bg_y - HEIGHT
  cvs.delete('all')
  cvs.create_image(240, bg_y-360, image=bg)
  cvs.create_image(240, bg_y+360, image=bg)
  cvs.create_image(p1_x, p1_y, image=mycar)
  root.after(3, main)

root = tkinter.Tk()
root.bind("<Motion>", move)
cvs = tkinter.Canvas(width=WIDTH, height=HEIGHT)
cvs.pack()
bg = tkinter.PhotoImage(file="image/bg.png")
mycar = tkinter.PhotoImage(file="image/car_red.png")
main()
root.mainloop()