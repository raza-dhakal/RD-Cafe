import tkinter

# ウィンドウ作成 
root = tkinter.Tk()
root.title("リリに質問") 
root.minsize(640, 480)  
root.option_add("*font", ["MS Pゴシック", 22])
# 画像表示
pimg = tkinter.PhotoImage(file="img/back.png")
canvas = tkinter.Canvas(bg="black", width=640, height=480)
canvas.place(x=0, y=0)
canvas.create_image(320, 240, image=pimg)
# テキストボックス表示
question = tkinter.Label(text="知りたいのは何分かな？", bg="white")
question.place(x=100, y=40)

#テキストボックス表示
entry = tkinter.Entry(width=12, bd=4)
entry.place(x=50, y=133)

# 質問ボタン表示
askbutton = tkinter.Button(text="聞く")
askbutton.place(x=260, y=125)
#答え表示
answer = tkinter.Label(text="..........", bg="white")
answer.place(x=115, y=235)

#イベソト設定
def ask_click():
  val = entry.get()
  minutes = float(val)
  hours = round(minutes/60, 2)
  answer["text"] = str(hours) +"時間だね！？"

askbutton["command"] = ask_click
#メインループ
root.mainloop()
