import re

def passcheck():
    while True:
        print('パスワードを入力してください')
        password = input() #まずはパスワードを入力させる

        #まずは8文字以上の英数字かどうかを確認する。
        #[a-zA-Z0-9]は一文字の英数字にマッチする。
        #{8,}はそれが8回以上繰り返される文字列にマッチする。
        passletter_regex = re.compile(r'[a-zA-Z0-9]{8,}') 
        if passletter_regex.search(password) == None: #もしマッチしなければ.searchメソッドはNoneを格納する
            continue

        #ちなみに強いパスワードをきちんと入力した場合、
        #passletter_regax.search(password)で作成されるリストにはパスワードがそのまま格納されている。（貪欲マッチなので）
        #逆に、以下の.searchメソッドで作成されるリストにはパスワードの一部分のみしか格納されていないので注意されたし。

        #それぞれ、小文字、大文字、数字が一文字以上含まれているかを確認している
        passlower_regax = re.compile(r'[a-z]{1,}')
        if passlower_regax.search(password) == None:
            continue

        passupper_regax = re.compile(r'[A-Z]{1,}')
        if passlower_regax.search(password) == None:
            continue

        passnumber_regex = re.compile(r'[0-9]{1,}')
        if passnumber_regex.search(password) == None:
            continue

        print('Completed! The password is strong.')
        break

passcheck()
