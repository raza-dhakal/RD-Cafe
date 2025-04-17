import tkinter
root = tkinter.Tk()
root.title("ゲームのステータス画面を作ろう")
cvs = tkinter.Canvas(width=960, height=640)
img = tkinter.PhotoImage(file="image/character1.png")
cvs.create_image(480, 320, image=img)
cvs.create_rectangle(540, 60, 900, 580, fill="black", outline="white", width=3)

ability = ["H.P", "腕力", "防御力","知力","精神力","素早さ"]
value = [1200, 800, 320, 9999, 3540, 780]

for i in range(6):
    y = 120+80*i
    cvs.create_text(640, y, text=ability[i], font=("Times New Roman", 20), fill="white")
    cvs.create_text(800, y, text=value[i], font=("Times New Roman", 24), fill="white")

cvs.pack()
root.mainloop()