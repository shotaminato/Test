import re

def strip():
    print('処理する文章を入力してください')
    word = input()
    print('文頭から削除したいワードを入力してください。（空白ならenterキーを押してください）')
    top_word = input()
    print('文尻から削除したいワードを入力してください。（空白ならenterキーを押してください）')
    last_word = input()

    if top_word == '' and last_word == '':
        strip_regex = re.compile(r'\s*(.+)\s*') #空白が０文字以上、文字が１文字以上、空白が０文字以上の正規表現の書き方。ここができたらこのセクションはおけ。
        if strip_regex.search(word) != None:
            word = strip_regex.search(word)
            print(word.group(1))
    
    elif top_word != '' and last_word != '':
        seiki = r'\s*' + top_word + r'(.+)' + last_word + r'\s*'
        strip_regex = re.compile(seiki)
        if strip_regex.search(word) != None:
            word = strip_regex.search(word)
            print(word.group(1))            

    elif top_word != '':
        seiki = r'\s*' + top_word + r'(.+)\s*'
        strip_regex = re.compile(seiki)
        if strip_regex.search(word) != None:
            word = strip_regex.search(word)
            print(word.group(1))            

    elif last_word != '':
        seiki = r'\s*(.+)' + last_word + r'\s*'
        strip_regex = re.compile(seiki)
        if strip_regex.search(word) != None:
            word = strip_regex.search(word)
            print(word.group(1))   
    else:
        print('Error!')

strip()