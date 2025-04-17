import tkinter

# ウィンドウ作成 
root = tkinter.Tk()
root.title("勇者募集中！") 
root.minsize(640, 520)  
root.option_add("*font", ["メイリオ", 14])

# 画像読み込み 
img1 = tkinter.PhotoImage(file="img/1.png")
img2 = tkinter.PhotoImage(file="img/2.png")
img3 = tkinter.PhotoImage(file="img/3.png")
img4 = tkinter.PhotoImage(file="img/4.png")
img5 = tkinter.PhotoImage(file="img/5.png")

# キャンバス作成 
canvas = tkinter.Canvas(root, width=640, height=480)
canvas.place(x=0, y=0)
canvas.create_image(320, 220, image=img1, tag="illust")

# ラベル配置 
serihu_text = tkinter.Label(text="王様「魔法を倒したら褒美をやるぞ！」")
serihu_text.place(x=160, y=10)
sys_text = tkinter.Label(text="褒美はいくらあげますか？\n（～9999ゴールドまで）", fg="red")
sys_text.place(x=180, y=380)

# エントリ作成
entry = tkinter.Entry(width=12)
entry.place(x=180, y=450)
gold_text = tkinter.Label(text="ゴールド")
gold_text.place(x=330, y=450)

# ボタン配置 
button = tkinter.Button(text="決定")
button.place(x=420, y=440)

# ボタンクリックイベント関数 
def btn_click():
    gold = float(entry.get())
    if gold < 5000:
        canvas.delete("illust")
        serihu_text["text"] = "忘れ願者は誰も来ませんでした。"
    elif gold < 6500:
        canvas.create_image(320, 220, image=img2, tag="illust")
        serihu_text["text"] = "エルフ「頑張ってみますね。」"
    elif gold < 8000:
        canvas.create_image(320, 220, image=img5, tag="illust")
        serihu_text["text"] = "魔女「よし、私に任せなさい！」"
    else:
        canvas.create_image(320, 220, image=img3, tag="illust")
        serihu_text["text"] = "勇者「そんな大金、よっぽど危険なんだ……。」\n関わらないでおこう。」"

# ボタンクリックと関数の関連付け 
button["command"] = btn_click

root.mainloop()