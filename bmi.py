import tkinter as tk


def calc(weight, height):
    return weight / (height ** 2)


def check(bmi):
    if bmi < 18.5:
        result = '低体重 (तेいたいじゅう)'  # Underweight
    elif bmi < 25.0:
        result = '普通体重 (ふつうたいじゅう)'  # Normal weight
    elif bmi < 30.0:
        result = '少し太っている (すこしふとっている)'  # Slightly overweight
    elif bmi < 35.0:
        result = '太り気味 (ふとりぎみ)'  # Overweight
    elif bmi < 40.0:
        result = '太っている (ふとっている)'  # Obese
    else:
        result = '太りすぎ (ふとりすぎ)'  # Severely obese
    return result


root = tk.Tk()
root.title('肥満度チェック (BMI チェック)')
root.geometry('300x200')


label_1 = tk.Label(root, text='体重 (たいじゅう):')  # Weight
label_2 = tk.Label(root, text='kg')
label_3 = tk.Label(root, text='身長 (しんちょう):')  # Height
label_4 = tk.Label(root, text='cm')
label_5 = tk.Label(root, text='体重と身長を入力してください。')  # Instruction


weight = tk.Entry(root, width=5)
height = tk.Entry(root, width=5)


def judgement():
    try:
     
        w = float(weight.get())
        h = float(height.get()) / 100  
        bmi = calc(w, h) 
        s = check(bmi) 
        s_2 = round(bmi, 1)  
        label_5['text'] = f'BMI: {s_2}, 肥満度: {s}' 
    except ValueError:
        label_5['text'] = '正しい数値を入力してください。'  


button = tk.Button(root, text='BMI 判定 (はんてい)', command=judgement)


label_1.grid(column=0, row=0, sticky=tk.E)
weight.grid(column=1, row=0)
label_2.grid(column=2, row=0, sticky=tk.W)

label_3.grid(column=0, row=1, sticky=tk.E)
height.grid(column=1, row=1)
label_4.grid(column=2, row=1, sticky=tk.W)

button.grid(column=0, row=2, columnspan=3)
label_5.grid(column=0, row=3, columnspan=3)

root.mainloop()