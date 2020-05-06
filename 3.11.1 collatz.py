import math

def collatz():
    print('Please, enter an integer.') #説明文
    integer = int(input()) #整数を入力
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
            print('This program have an error, getting' + str(integer) + '.')
            break

collatz()
