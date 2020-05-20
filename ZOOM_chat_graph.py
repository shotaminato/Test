#!/usr/bin/env python3
#ZOOM_chat.py

import re, pyperclip, tkinter
from tkinter import messagebox

def tp():
    text =input_box.get()
    text_regex = re.compile(r'\d\d:\d\d:\d\d\s\s開始\s?[A-Z]?-?\d?\d?-?\d?\d?[-]?\s?\s?[-]?(.*)')
    sentence_list = text_regex.findall(text)
    new_text = '・' + '\n・'.join(sentence_list)
    letters = ''
    for i in range(len(new_text)):
        if new_text[i] == '，':
            letters += '、'
            print (str(new_text[i]))
        elif new_text[i] == '．':
            letters += '。'
        else:
            letters += str(new_text[i])
        
    pyperclip.copy(letters)
    messagebox.showinfo('以下の文章をクリップボードにコピーしました', letters)

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


