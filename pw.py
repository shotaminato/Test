#! python3
pt
PASSWORDS = {'email' : 'F7minlBDDuvMJuxESSKHhTxFtjVB6',
             'blog' : 'VmALvQyKAxiVH5G8v0lif1MLZ3sdt',
             'luggage' : '12345'}

import sys
import pyperclip

if len(sys.argv) < 2 :
    print('使い方： python pw.py [アカウント名]')
    print('パスワードをクリップボードにコピーします')
    sys.exit()

account = sys.argv[1] # 最初のコマンドライン引数がアカウント名
# 別にわざわざ変数に代入して使う必要はないのだけれど、sys.argv[1]だけだと、
# 一体何を指しているのか分からないので、分かりにくいソースコードになる。

if account in PASSWORDS: #PASSWORDは辞書型なので、PASSWORDS.keys()と書くのが正式
    pyperclip.copy(PASSWORDS[account])
    print(account + 'のパスワードをクリップボードにコピーしました')
else:
    print(account + 'というアカウント名はありません')

