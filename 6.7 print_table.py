#! /usr/bin/env python3
#↑Mac専用の一行。別になくても大丈夫。

table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]
#今回はこういうデータがあるということにしよう。本当はこのリストの入力プログラムから作るのがいいかな。

def print_table(data):    #まずは簡単にするために、単に並べるプログラムを作ろう。
    for i in range(len(data[0])):    #横の長さを取得する。全部一緒（４）なので[0]を採用。
        for j in range(len(data)):
            print (str(data[j][i]) + ' ', end = '')
        print('')

def r_align(data):    #右揃えで整列するプログラムを作ろう。
    for i in range(len(data)): 
        letter_number = 0   #次の作業のために、新変数を定義して初期化
        for j in range(len(data[0])):    #まずはそれぞれの”列”の最大文字数を取得する
            if letter_number < len(data[i][j]):    #上のとi, jが逆だぞ。
                letter_number = len(data[i][j])
        for j in range(len(data[0])): 
            
            data[i][j] = data[i][j].rjust(letter_number)    #元のデータを右揃えした文字列で置き換える。
    return(data)    #完成したリストを返す。


table_data = r_align(table_data) #まずは文字数を揃えたリストに置き換える。
print_table(table_data)    #リストを表示する