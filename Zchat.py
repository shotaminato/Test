#!/usr/bin/env python3
#ZOOM_chat.py

import re, pyperclip, tkinter
from tkinter import messagebox

def tp():
    #テキストボックスからインプット
    text =input_box.get()

    #余計な部分を検索し、・に置き換え。
    text_regex = re.compile(r'\d\d:\d\d:\d\d\s\s開始\s?[A-Z]?-?\d?\d?-?\d?\d?[-]?\s?\s?[-]?')
    new_text = text_regex.sub('・', text)
   
    #カンマとコロンを置き換え
    comma_regex = re.compile('，')
    period_regex = re.compile('．')
    new_text = comma_regex.sub('、', new_text)
    new_text = period_regex.sub('。', new_text)
    
    #クリップボードと画面に出力
    pyperclip.copy(new_text)
    messagebox.showinfo('以下の文章をクリップボードにコピーしました', new_text)

#ウインドウの作成
root = tkinter.Tk()
root.title("ZOOMchat処理")
root.geometry("480x240")

#入力欄の作成
input_box = tkinter.Entry(width=40)
input_box.place(x=10, y=100)

#ラベルの作成
input_label = tkinter.Label(text="処理したい文章を以下にペーストして、実行ボタンを押してください")
input_label.place(x=10, y=70)

#ボタンの作成
button = tkinter.Button(text="実行",command=tp)
button.place(x=300, y=130)

#ウインドウの描画
root.mainloop()


