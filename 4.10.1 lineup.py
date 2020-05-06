def make_list(): #まずはリストを作る関数を定義する（見やすくするため）
    list_one = []　#この一文がないとappendメソッドでエラーになる
    while True :   
        print('Please, enter something. Press "enter" to finish.')
        added = input() #好きな文字を入力させる
        list_one.append(added) #リストの最後に入力した文字を追加する
        if list_one[-1] == '' : #while終了処理。今回はエンターを押させているのでこの条件
            del list_one[-1] #余計な要素('')を消す
            break 
    print(list_one) #確認のため作ったリストを画面出力
    return(list_one) #リストを戻り値として渡す

def line_up():
    list_one = make_list() #さっきの関数を動かす
    screen = ''
    for i in range(len(list_one) - 1) : #最後の一つ手前までforループ
        screen += str(list_one[i]) + ', ' #リストの要素が文字数型とは限らないのでstr()を入れる
    screen += 'and ' + str(list_one[-1]) #最後の一つのやつ
    print(str(screen))

line_up()