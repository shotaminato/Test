import math

def collatz():
    print('Please, enter an integer.') #説明文

    #3.11.2の追加分
    while True:
        try :
            integer = int(input()) 
        except ValueError : #inputに整数以外を入れるとこのエラーが起きるので例外処理する
            print('Please enter an INTEGER.') #警告文
            continue #except処理されたら強制的にwhile続行
        break #exceptされなかったらwhile終了

    print('You entered ' + str(integer) + '.' )

    while True : #無限ループを発生させる（練習）
        if integer % 2 == 0 : #偶数の時の処理
            integer = integer / 2
            print(integer)
        elif integer == 1 : #終了処理
            print('Completed!')
            break
        elif integer % 2 == 1 : #奇数の時の処理
            integer = integer * 3 + 1
            print(integer)
        else : #エラー時の警告
            print('This program have an error, \
                getting' + str(integer) + '.')
            break

collatz()
